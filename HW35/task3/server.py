import socket
import multiprocessing

HOST = '127.0.0.1'
PORT = 5050


def listen_client(conn, addr):
    with conn:
        print(f"A new client has connected: {addr}:")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"The server has received the data {addr}: {data}")
            response = data
            print(f"The server sends data to the client{addr}: {response}")
            conn.send(response.encode())


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"The server with the address {HOST, PORT} is running and waiting for new connections...")
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            p1 = multiprocessing.Process(target=listen_client, args=(conn, addr))
            p1.start()