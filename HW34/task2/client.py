import socket

HOST: str = '127.0.0.1'  # '0.0.0.0', 'localhost'
PORT: int = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break
        print(f"Send message {message}")
        response = client_socket.recv(1024)
        print(f"I receive response: {response.decode('utf-8')}")