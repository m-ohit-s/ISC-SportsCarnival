import socket


class JsonClient:

    def __init__(self, host, port, size, encoding_format):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.size = size
        self.encoding_format = encoding_format

    def connect_server(self):
        self.client_socket.connect((self.host, self.port))
        return self.client_socket

    def start_communication(self, data: str):
        self.client_socket.sendall(data.encode(self.encoding_format))
        response_data = self.client_socket.recv(int(self.size)).decode(self.encoding_format)
        print(f"Received from server: {response_data}")

    def disconnect_server(self):
        self.client_socket.close()
