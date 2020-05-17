#!/bin/python3

import sys # for command-line args
import socket
from datetime import datetime

# defining our target
if(len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of args")
    print("Syntax:./port-scanner.py 192.168.0.2")
    sys.exit()

#Starting
print("-"*50)
print(f"Scanning target : {target}")
print(f"Time Started : {datetime.now()}")
print("-"*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print(f"Checking port :: {port}")

        if(result==0):
            print(f"Port:: {port} is open")
        elif(result==111):
            print("Connection Refused By Host")
            break
        s.close()


except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

except socket.gaierror:
    print("Hostname cannot be rosolved")
    sys.exit()

except socket.error():
    print("server is down")
    sys.exit()

