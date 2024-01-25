import asyncio
import socket

HOST = '127.0.0.1'
PORT = 5050


async def handle_client(conn, addr):
    try:
        print(f"A new client has connected: {addr}:")
        while True:
            data = (await loop.sock_recv(conn, 1024)).decode()
            if not data:
                break
            print(f"The server has received the data {addr}: {data}")
            response = data
            print(f"The server sends data to the client{addr}: {response}")
            conn.send(response.encode())
    finally:
        conn.close()



async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"The server with the address {HOST}:{PORT} is running and waiting for new connections...")

    while True:
        conn, addr = await loop.sock_accept(server_socket)
        loop.create_task(handle_client(conn, addr))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())