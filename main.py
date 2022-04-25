#! /usr/bin/env python3

import socket

#address = input("IP: ")
#port = input("Port: ")

address = '127.0.0.1'
port = 80
message = 'Test'
buffer = 1024
error = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((address, port))
except socket.error as e:
    print(e)
    error = True

if error == False:

    s.send(message.encode())

    data =  s.recv(buffer)

    print(data.decode())
