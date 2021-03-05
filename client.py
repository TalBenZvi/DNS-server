import sys
import socket

def main(argv):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        request = input()
        s.sendto(bytes(request, encoding='utf8'), (argv[1], int(argv[2])))
        data, addr = s.recvfrom(1024)
        ip = data.decode("utf-8").split(",")[1]
        print(ip)

main(sys.argv)