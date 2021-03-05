import sys
import socket
from datetime import datetime
from datetime import timedelta

def main(argv):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', int(argv[1])))
    """
    a second socket is used to separate the client requests and 
    the answers from the parent server
    """
    parent_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data, addr = s.recvfrom(1024)
        request = data.decode("utf-8") 
        is_in_database = False
        ips = open(argv[4], "r+")
        lines = ips.readlines()
        for line in lines:
            parameters = line.strip("\n").split(",")
            if (request == parameters[0]):
                """
                lines that contain adresses that the server has studied will have a fourth
                parameter to indicate when the line was studied.
                """
                if (len(parameters) == 3):
                    is_in_database = True
                    s.sendto(bytes(line, encoding='utf8'), addr)
                else:
                    now = datetime.now()
                    save_time = datetime.strptime(parameters[3], '%Y-%m-%d %H:%M:%S.%f')
                    ttl = timedelta(seconds=int(parameters[2]))
                    if now - save_time <= ttl:
                        is_in_database = True
                        s.sendto(bytes(line.rsplit(',', 1)[0], encoding='utf8'), addr)
                    else:
                        # deleting the line from the file
                        ips.seek(0)
                        for checked_line in lines:
                            if checked_line != line:
                                ips.write(checked_line)
                        ips.truncate()
        ips.close()
        if not is_in_database:
            # ask the parent server for the adress and add it to the file
            parent_socket.sendto(data, (argv[2], int(argv[3])))
            data_from_parent, parent_addr = parent_socket.recvfrom(1024)
            s.sendto(data_from_parent, addr)
            ips = open(argv[4], "a")
            ips.write("\n" + data_from_parent.decode("utf-8").strip("\n")  + "," + str(datetime.now()))
            ips.close()

main(sys.argv)