import sys
import socket
from termcolor import colored, cprint

def check(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(ip + ":" + str(port), end="")
        cprint(" OPEN", 'green')
    else:
        print(ip + ":" + str(port), end="")
        cprint(" CLOSE", 'red')

with open(sys.argv[1]) as f:
    for line in f:
        ip = line.strip("\n").split(";")[0]
        ports = list(map(lambda x: int(x), line.strip("\n").split(";")[1:]))
        for port in ports:
            check(ip, port)
