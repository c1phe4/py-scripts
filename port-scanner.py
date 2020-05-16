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
        
        print(result)

        if(result==0):
            print(f"Port:: {port} is open")
        s.close()

except KeyBoardInterrupt:
    print("Exiting...")
    sys.exit()
