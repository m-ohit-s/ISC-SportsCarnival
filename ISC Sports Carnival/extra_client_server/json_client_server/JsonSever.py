import json
import socket
import threading


class JsonServer:
    def __init__(self, host, port, size, encoding_format):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.__size = size
        self.__encoding_format = encoding_format
        self.__client_data = ""

        self.__server_socket.bind((host, port))

    def start_server(self):
        self.__server_socket.listen()
        print(f"server is listening ...")

    def accept_client(self):
        conn, addr = self.__server_socket.accept()
        print(f"Connection started from: {str(addr)}")
        thread = threading.Thread(target=self.__handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections {threading.active_count() - 1}")
        return conn, addr

    def __handle_client(self, conn, addr):
        print(f"new connection {addr} connected")
        connected = True
        while connected:
            self.__client_data = conn.recv(int(self.__size)).decode(self.__encoding_format)
            if not self.__client_data:
                connected = False
            print(f"[{addr}] {self.__client_data}")
            conn.send(self.__client_data.encode(self.__encoding_format))
        return conn

    def get_client_data(self):
        return self.__client_data

    def send_response(self, response_data: str, conn):
        conn.send(response_data.encode(self.__encoding_format))

    @staticmethod
    def close_connection(conn):
        conn.close()
