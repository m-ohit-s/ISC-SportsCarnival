import socket


class EchoClient:

    def __init__(self, host, port, size, encoding_format, disconnect_msg):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.size = size
        self.encoding_format = encoding_format

    def connect_server(self):
        self.client_socket.connect((self.host, self.port))
        return self.client_socket

    def send_msg(self, msg):
        self.client_socket.send(msg.encode(self.encoding_format))
        data = self.client_socket.recv(int(self.size)).decode(self.encoding_format)
        print(f"Received from server: {data}")
        msg = input("> ")
        return msg

    def disconnect_server(self):
        self.client_socket.close()
