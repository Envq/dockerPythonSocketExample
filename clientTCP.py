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

# Create a TCP socket at client side
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("TCP client ready")
    s.connect((HOST, PORT))
    print("TCP client connected to server {}:{}".format(HOST, PORT))
    # Listen for incoming data from User
    while(True):
        message = input("Send messagge: ")
        data = str.encode(message)
        s.send(data)
        # Get server response
        response = s.recv(1024)
        print("> {}".format(response.decode()))
        # Check close message
        if message == "close":
            print("Client closed")
            break