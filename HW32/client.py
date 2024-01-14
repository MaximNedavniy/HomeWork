import json
import socket

HOST = '127.0.0.1'
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    message = input("Enter a message for the server: ")
    key = int(input("Enter the key for Caesar's cipher: "))
    data_to_send = {'message': message, 'key': key}
    json_data = json.dumps(data_to_send)
    client_socket.sendto(json_data.encode(), (HOST, PORT))
    data, server_addr = client_socket.recvfrom(1024)
    print(f"Response from the server: {data.decode()}")
