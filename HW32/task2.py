#server
import json
import socket
import cesar
HOST='127.0.0.1'
PORT=5000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    while True:
        data, client_address = server_socket.recvfrom(1024)

        data_dict = json.loads(data.decode())

        message = data_dict['message']
        key = data_dict['key']

        response_message = cesar.caesar_encryption(key, message)

        if not data:
            break
        server_socket.sendto(response_message.encode(), client_address)