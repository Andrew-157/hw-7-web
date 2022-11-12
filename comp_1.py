import socket

HOST = '127.0.0.1'
PORT = 55555

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((HOST, PORT))
sock.listen(1)
sock_name = sock.getsockname()
print(f"Opening socket: {sock_name}")

connection, address = sock.accept()
print(f"Established connection with {address}")

while True:

    data = connection.recv(1024)

    if data:
        print(f"Message from client: {data.decode()}")
        connection.send(b'Ok')
        break

connection.close()


with socket.socket() as sock:
    sock.connect((HOST, PORT))
    print("Connected to server...")
    sock.sendall(b'Message')
    print("Client sent message")

    data = sock.recv(1024)

    if data:
        print(f"Got message from server: {data.decode()}")
