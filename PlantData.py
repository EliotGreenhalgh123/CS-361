import socket
import json

plant_data = {
    1: "Here is some information about plant 1",
    2: "Here is some information about plant 2",
    3: "Here is some information about plant 3",
    4: "Here is some information about plant 4",
    5: "Here is some information about plant 5",
    6: "Here is some information about plant 6",
    7: "Here is some information about plant 7"
    }


def data_server():
    """
    Server that allows for microservice to communicate with data file. Takes no parameters and returns no values.
    Creates a JSON object of the plant data that is sent via socket to the microservice.
    """

    host = '127.0.0.1'
    port = 2500

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    while True:

        data = conn.recv(1024).decode()
        data = int(data)

        if data == 1:

            # create JSON object from plant dictionary
            data_to_send = str.encode(json.dumps(plant_data))

            # send data to microservice
            conn.sendall(data_to_send)
            break

    conn.close()


data_server()
