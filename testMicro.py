"""
This file is not part of the microservice, but is used to test the service. Final program will include a client-side
implementation similar to this.

Note: There is no input validation. For testing, use integer inputs 1-7

This file prompts the user to input a valid plant ID number. The ID will be sent to the microservice, where the
corresponding information will be determined. The corresponding information will be sent back here.
"""

import socket

# arbitrary port number
host = '127.0.0.1'
port = 2100

# basic socket implementation
client_socket = socket.socket()
client_socket.connect((host, port))

plantID = input("Enter a plant ID: ")
client_socket.send(plantID.encode())
data = client_socket.recv(1024).decode()
print(f'Data for plant {plantID}: ' + data)

client_socket.close()
