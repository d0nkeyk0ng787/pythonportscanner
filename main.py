#! /usr/bin/env python3

# NOTE - I removed the multiprocessing functionality because whilst it works there are some inherent issues with doing port scanning on multiple threads

import sys
import time
import socket
import argparse
#import multiprocessing

if len(sys.argv) == 2:
    address = sys.argv[1]
else:
    print("Invalid number of arguments passed. Ensure you entered an IP address to scan.")
    sys.exit()

start = time.time()
welcome = "Gnomes port scanner - Written in python - Scan will now begin"
scanning = "Now scanning " + address

def scanports(a, b, address):

    aliveports = []
    
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

    x = len(aliveports)

    return address, x


def finish(address, portcount):

    end = time.time()
    timetaken = (end - start)
    scandonemessage = (f"Portscan Completed | 1 IP Address {address} scanned | There are {portcount} alive ports | Scan completed in {round(timetaken, 4)} seconds")

    print(scandonemessage)
    sys.exit()


if __name__ == "__main__":

    print(welcome)
    print(scanning)
    
    #p1 = multiprocessing.Process(target=scanports, args= [1, 10])
    #p2 = multiprocessing.Process(target=scanports, args= [251, 500])
    #p3 = multiprocessing.Process(target=scanports, args = [501, 750])
    #p4 = multiprocessing.Process(target=scanports, args= [751, 1024])

    #p1.start()
    #p2.start()
    #p3.start()
    #p4.start()

    #p1.join()
    #p2.join()
    #p3.join()
    #p4.join()

    addy, x = scanports(1, 10, address)

    finish(addy, x)
