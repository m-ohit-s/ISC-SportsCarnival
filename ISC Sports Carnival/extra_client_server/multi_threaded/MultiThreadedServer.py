import socket
import threading


class MultiThreadedServer:
    def __init__(self, host, port, size, encoding_format, disconnect_msg):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind((host, port))
        self.__host = host
        self.__port = port
        self.__size = size
        self.__encoding_format = encoding_format
        self.__disconnect_msg = disconnect_msg
        self.__is_server_active = True
        # self.__stop_server_command = "stop"

    def start_connection(self):
        self.__server_socket.listen(2)
        print(f"Server is listening at {self.__host}:{self.__port}")
        self.__accept_client()
        # self.__stop_server()
        return

    # def __stop_server(self):
    #     stop_server_command = input("> ")
    #     if stop_server_command == self.__stop_server_command:
    #         self.__server_socket.sendall("Server Stopped ...".encode(self.__encoding_format))
    #         self.__server_socket.close()
    #         exit(0)

    def __accept_client(self):
        while self.__is_server_active:
            conn, addr = self.__server_socket.accept()
            print(f"Connection started from: {str(addr)}")
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"Active Connections {threading.active_count() - 1}")
            # self.__stop_server()
        return

    def handle_client(self, conn, addr):
        print(f"new connection {addr} connected")
        connected = True
        while connected:
            data = conn.recv(int(self.__size)).decode(self.__encoding_format)
            if data is self.__disconnect_msg:
                connected = False
            print(f"[{addr}] {data}")
            print(f"msg from client: {data}")
            conn.send(data.encode(self.__encoding_format))
        return conn

    @staticmethod
    def close_connection(conn):
        conn.close()
