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

# Create a TCP socket at server side
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen() # enable to accept connection
    print("TCP server ready")
    # Wait connection
    conn, client = s.accept()
    clientAddr = client[0]
    clientPort = client[1]
    print("TCP server connected to client {}:{}".format(clientAddr, clientPort))
    with conn:
        while (True):
            # Get messages
            data = conn.recv(1024)
            message = data.decode()
            print("> {}".format(message))
            # Send responde
            conn.send(str.encode("Received: '{}'".format(message)))
            # Check close message
            if message == "close":
                print("Server closed")
                break