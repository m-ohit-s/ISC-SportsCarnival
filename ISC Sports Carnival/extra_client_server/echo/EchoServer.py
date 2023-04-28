import socket


class EchoServer:
    def __init__(self, host, port, size, encoding_format, disconnect_msg):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind((host, port))
        self.__host = host
        self.__port = port
        self.__size = size
        self.__encoding_format = encoding_format
        self.__disconnect_msg = disconnect_msg

    def start_connection(self):
        self.__server_socket.listen(2)
        print(f"Server is listening at {self.__host}:{self.__port}")
        conn, addr = self.__server_socket.accept()
        print(f"Connection started from: {str(addr)}")

        while True:
            data = conn.recv(int(self.__size)).decode(self.__encoding_format)
            if not data:
                break
            print(f"msg from client: {data}")
            data = input(' -> ')
            conn.send(data.encode(self.__encoding_format))
        return conn

    @staticmethod
    def close_connection(conn):
        conn.close()
