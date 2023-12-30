#server
import socket

HOST='127.0.0.1'
PORT=5000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    while True:
        data, client_address = server_socket.recvfrom(1024)
        if not data:
            break
        server_socket.sendto(data, client_address)