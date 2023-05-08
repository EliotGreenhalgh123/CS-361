Microservice Implementation - Communication Contract

To request data from the microservice, a client socket must be first initialized, as seen in the testMicro.py file in the demonstration video. The port number is arbitrary (above 1024), but this client socket must have the same port number as the server_program() function within the MicroserviceServer.py file. As long as this connection is made, communication is relatively straightforward. With the MicroserviceServer.py and PlantData.py files running, run the testMicro.py file and you will be prompted to input an integer key value (1 through 7).

Ex.
Enter a plant ID: 5

Will return the corresponding information for plant 5 in the dictionary. 

Data from the microservice will be returned via socket to the client socket located within the main program. In the testMicro.py file, this variable is simply called 'data'. In this file, the data is printed to the terminal. However, it would be easy to save this variable and use it as necessary within the full program. 

