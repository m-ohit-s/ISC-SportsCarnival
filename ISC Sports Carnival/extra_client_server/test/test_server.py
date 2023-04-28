import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("ITT-MOHITSA", 5000))

server_socket.listen()
print("server is listening ...")

conn, addr = server_socket.accept()

while conn:
    data = conn.recv(1024).decode("utf-8")
    print(data)
    if not data:
        break
    conn.sendall(bytes(data.encode("utf-8")))
