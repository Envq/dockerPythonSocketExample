#!/usr/bin/env python3
import socket
import sys

# Connection config
HOST = "server"
PORT = 2000

# Update HOST
if (len(sys.argv) == 2):
    HOST = sys.argv[1]
if (len(sys.argv) == 3):
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
print("Selected: -> {}:{}".format(HOST,PORT))

# Create a UDP socket at server side
with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP server ready")
    # Manage message
    while(True):
        # Get message
        data, client = s.recvfrom(1024)
        message = data.decode()
        clientAddr = client[0]
        clientPort = client[1]
        print("[{}:{}]: {}".format(clientAddr, clientPort, message))
        # Check close message
        if message == "close":
            print("Server closed")
            break