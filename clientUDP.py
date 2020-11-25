#!/usr/bin/env python3
import socket
import sys

# Connection config
HOST = "server"
PORT = 32768

# Update HOST
if (len(sys.argv) == 2):
    HOST = sys.argv[1]
if (len(sys.argv) == 3):
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
print("Selected: -> {}:{}".format(HOST,PORT))


# Create a UDP socket at client side
with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    print("UDP client ready")

    # Listen for incoming data from User
    while(True):
        message = input("Send messagge: ")
        data = str.encode(message)
        s.sendto(data, (HOST, PORT))
        # Check close message
        if message == "close":
            print("Client closed")
            break