import json
import socket
import threading

from communication_protocol.ICSRequest import ICSRequest
from communication_protocol.RequestResponseHandler import RequestResponseHandler
from core.client_server.command_controller.CommandController import CommandController
from utils.json_encoder.ObjectEncoder import ObjectEncoder


class MainServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()

    def start(self):
        print("server is listening ...")
        while True:
            client_socket, address = self.socket.accept()
            print(f"client connected {self.host} - {self.port}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        data = client_socket.recv(1024).decode("utf-8")
        request = json.loads(data)
        request_obj = ICSRequest.from_dict(request)
        data_list = request_obj.data
        data_format = request_obj.protocol_format
        processed_data = self.process_data(data_list[0], data_list[1], data_format, data_list[2])
        response = RequestResponseHandler.create_response(processed_data, request_obj)
        response_data = json.dumps(response, cls=ObjectEncoder)
        client_socket.send(response_data.encode("utf-8"))

    def process_data(self, input_command, data, file_format, output_file_location):
        # Process the data here
        command_controller = CommandController()
        processed_data = command_controller.server_action_commands(
            input_command,
            data,
            file_format,
            output_file_location
        )
        return processed_data

    def get_data_from_client(self):
        return self.socket.recv(1024).decode("utf-8")

    def stop(self):
        return self.socket.close()
