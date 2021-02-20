import socket
from datetime import datetime
from datetime import timedelta

def main(argv):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', argv[1]))
    ips = open(argv[4], "r")

    parent_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data, addr = s.recvfrom(1024)
        request = str(data)
        is_in_database = False
        for line in ips:
            parameters = line.split(",")
            if (request == parameters[0]):
                if (parameters.length() == 3):
                    is_in_database = True
                    s.sendto(parameters[1], addr)
                else:
                    now = datetime.now()
                    save_time = datetime.strptime(parameters[3], '%Y-%m-%d %H:%M:%S')
                    ttl = timedelta(seconds=int(parameters[2]))
                    if now - save_time <= ttl:
                        is_in_database = True
                        s.sendto(parameters[1], addr)
        if not is_in_database:
            parent_socket.sendto(data, (argv[2], argv[3]))
            ip, parent_addr = parent_socket.recvfrom(1024)
            




    """
    today = datetime.strptime("2019-09-18 01:55:19", '%Y-%m-%d %H:%M:%S')
    yesterday = datetime.strptime("2019-09-18 01:52:19", '%Y-%m-%d %H:%M:%S')
    print(today)
    print(yesterday)
    if today - yesterday < timedelta(seconds=181):
        print("yes")
    else:
        print("no")
        """


main(0)