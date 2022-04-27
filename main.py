#! /usr/bin/env python3

import socket
import time

#address = input("IP: ")
#port = input("Port: ")

address = '127.0.0.1'
aliveports = []
timetaken = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = time.time()

with open('well-known-ports.txt', 'r') as f:
    for i in f:
        s_i = i.strip()
        s_i = int(s_i)
        error = False
        
        try:
            s.connect((address, s_i))
        except socket.error as e:
            #print(e)
            error = True
            #print(f"Port {s_i} is down")

        if error == False:

            s.close()
            
            aliveports.append(s_i)
            print(f"Port {s_i} is alive")

    end = time.time()
    timetaken = (end - start)

    apcount = len(aliveports)
    scandonemessage = (f"Portscan Completed | 1 IP Address {address} scanned | There are {apcount} alive ports | Scan completed in {timetaken} seconds")

    print(scandonemessage)
    #print(aliveports)
