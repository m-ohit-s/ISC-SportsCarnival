import json
import socket
import threading

import select

from communication_protocol.ICSRequest import ICSRequest
from communication_protocol.RequestResponseHandler import RequestResponseHandler
from core.client_server.command_controller.CommandController import CommandController
from utils.custom_logger.CustomLogger import CustomLogger
from utils.json_encoder.ObjectEncoder import ObjectEncoder


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        self.clients = []
        self.logger = CustomLogger()

    def start(self):
        print("server is listening ...")
        self.logger.debug("server is listening")
        while True:
            client_socket, address = self.socket.accept()
            self.logger.debug(f"Connected to {address}")
            print(f"Connected to {address}")
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = self.recv_all(client_socket, 128, 1000).decode("utf-8")
                if not data:
                    break
                print(f"received: {data}")
                self.logger.debug(f"received:  {data}")
                json_data = json.loads(data)
                if json_data.get("action") == "quit":
                    client_socket.send("Server is closing the connection".encode())
                    self.logger.info(f"Server is closing the connection")
                    print(f"Server is closing the connection")
                    print(client_socket)
                    self.clients.remove(client_socket)
                    print()
                    client_socket.close()
                    break
                else:
                    request = ICSRequest.from_dict(json_data)
                    data_list = request.data
                    data_format = request.protocol_format
                    processed_data = self.process_data(data_list[0], data_list[1], data_format, data_list[2])
                    response = RequestResponseHandler.create_response(processed_data, request)
                    response_data = json.dumps(response, cls=ObjectEncoder)
                    self.logger.debug(f"response: {response_data}")
                    print("response data:", response_data)
                    client_socket.send(response_data.encode())

            except ConnectionResetError:
                self.logger.error(f"Connection Reset From the server")
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def process_data(self, input_command, data, file_format, output_file_location):
        command_controller = CommandController()
        processed_data = command_controller.server_action_commands(
            input_command,
            data,
            file_format,
            output_file_location
        )
        return processed_data

    def stop(self):
        for client_socket in self.clients:
            client_socket.send("Server is closing the connection".encode())
            self.logger.debug(f"Server is closing the connection: {client_socket}")
            client_socket.close()
        self.socket.close()
        self.logger.debug(f"Connection Closed")

    def recv_all(self, client_socket, buffer_size, timeout=None):
        chunks = []
        client_socket.setblocking(0)
        while True:
            ready = select.select([client_socket], [], [], timeout)
            if not ready[0]:
                return None

            data = client_socket.recv(buffer_size)
            self.logger.debug(f"Data is sent in buffer size: {buffer_size}")
            # print(data)
            if not data:
                break
            chunks.append(data)
            if len(data) < buffer_size:
                break
        client_socket.setblocking(1)
        return b''.join(chunks)
