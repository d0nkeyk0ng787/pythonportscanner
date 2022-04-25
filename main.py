#! /usr/bin/env python3

import socket

#address = input("IP: ")
#port = input("Port: ")

address = '127.0.0.1'
port = [21, 22, 80, 8080]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in port:

    error = False
    
    try:
        s.connect((address, i))
    except socket.error as e:
        #print(e)
        error = True
        print(f"Port {i} is down")


    if error == False:

        s.close()
        
        print(f"Port {i} is alive")
