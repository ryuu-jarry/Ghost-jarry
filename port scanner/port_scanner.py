#!/usr/bin/python3

import socket
import sys
import time
import threading
from colorama import Fore

usege = f'{Fore.RED}python3 port_scan.py TARGET START_PORT END_PORT'
print(f'{Fore.RED}_'*70)
print()
print(f'{Fore.YELLOW}PYTHON SIMPLE PORT SCANNER')
print(f'{Fore.RED}_'*70)
print()

start_time = time.time()

if(len(sys.argv) != 4):
    print(usege)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])

except socket.gaierror:
    print('Name resolution error')
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print('Scanning target',target)

def scan_port(port):
    #print('Scanning port',port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((target, port))
    if(not conn):
        print(f'{Fore.BLUE}Port {port} is open')

for port in range(start_port,end_port+1):
    thread = threading.Thread(target=scan_port, args= (port,))
    thread.start()
end_time = time.time()
print(f'{Fore.RED}Time Elapsed::',end_time - start_time)