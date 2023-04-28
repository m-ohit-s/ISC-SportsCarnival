import json
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("ITT-MOHITSA", 5000))

data = {"hello": "world"}
data = json.dumps(data)
client_socket.sendall(bytes(data.encode("utf-8")))
data = client_socket.recv(1024).decode("utf-8")
print("Received: %s" % data)

client_socket.close()