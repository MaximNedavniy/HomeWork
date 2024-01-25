import asyncio
import socket

HOST = '127.0.0.1'
PORT = 5050


async def receive_messages(client_socket):
    while True:
        data = await loop.sock_recv(client_socket, 1024)
        if not data:
            break
        print(f"Message received: {data.decode('utf-8')}")

async def send_messages(client_socket):
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))
        await asyncio.sleep(0.1)
        if message.lower() == 'exit':
            break

async def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        receive_task = asyncio.create_task(receive_messages(client_socket))
        send_task = asyncio.create_task(send_messages(client_socket))
        await asyncio.gather(receive_task, send_task)
    finally:
        client_socket.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
