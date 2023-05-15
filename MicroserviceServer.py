"""
Main microservice file
"""


import json
import socket


def server_program():
    """
    Facilitates communication between main program and microservice. Receives plantID number via socket, and returns
    the corresponding information from the plant data structure.

    Takes no parameters and returns no values
    """

    host = '127.0.0.1'
    port = 2100

    # simple socket server-side implementation
    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    while True:

        data = conn.recv(1024).decode()

        if not data:
            break

        print("Request: " + str(data))

        # initiate contact with data file
        all_data = fetch_data()

        # load JSON file
        all_data = json.loads(all_data)
        print(all_data)

        # return dictionary value at key plantID
        requested = all_data.get(data)

        conn.send(requested.encode())

    conn.close()


def fetch_data():
    """
    Contacts the data file. Establishes a separate socket connection with data file
    """

    host = '127.0.0.1'
    port = 2500

    # simple socket implementation
    client_socket = socket.socket()
    client_socket.connect((host, port))

    data_to_send = "1"

    client_socket.send(data_to_send.encode())

    data = client_socket.recv(1024).decode()

    client_socket.close()

    return data


server_program()
