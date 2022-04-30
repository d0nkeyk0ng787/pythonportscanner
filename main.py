#! /usr/bin/env python3

# TODO - Add multithreading / UNFUCK multithreading implementation
# TODO - Fix the printing of the completed message

import sys
import time
import socket
import multiprocessing

#address = input("IP: ")
#port = input("Port: ")

start = time.time()

def scanports(a, b):

    address = '127.0.0.1'
    aliveports = []
    timetaken = 0
    
    try:
        for i in range(a, b):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            res = s.connect_ex((address, i))
            if res == 0:
                aliveports.append(i)
                print(f"Port {i} is alive")
            s.close()

    except socket.gaierror:
        print("Hostname could not be reached")
        sys.exit()
    except socket.error:
        print("Host unresponsive")
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()

    end = time.time()
    timetaken = (end - start)
    apcount = len(aliveports)
    scandonemessage = (f"Portscan Completed | 1 IP Address {address} scanned | There are {apcount} alive ports | Scan completed in {round(timetaken, 4)} seconds")
    
    print(scandonemessage)
    sys.exit()

def finish():
    pass


if __name__ == "__main__":
    
    p1 = multiprocessing.Process(target=scanports, args= [1, 250])
    p1.start()
    p1.join()

    p2 = multiprocessing.Process(target=scanports, args= [251, 500])
    p2.start()
    p2.join()

    p3 = multiprocessing.Process(target=scanports, args = [501, 750])
    p3.start()
    p3.join()

    p4 = multiprocessing.Process(target=scanports, args= [751, 1024])
    p4.start()
    p4.join()

    #print(aliveports)
