import json
import socket
import threading

from core.client_server.command_controller.CommandController import CommandController
from utils.json_encoder.ObjectEncoder import ObjectEncoder


class TeamServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()

    def start(self, input_command, file_format, output_file_location):
        print("server is listening ...")
        while True:
            client_socket, address = self.socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, input_command, file_format, output_file_location))
            client_thread.start()

    def handle_client(self, client_socket, input_command, file_format, output_file_location):
        data = client_socket.recv(1024)
        processed_data = self.process_data(data, input_command, file_format, output_file_location)
        response = self.create_response(processed_data)
        print(type(response))
        client_socket.send(json.dumps(response, indent=4, cls=ObjectEncoder).encode("utf-8"))
        client_socket.close()

    def process_data(self, data, input_command, file_format, output_file_location):
        # Process the data here
        command_controller = CommandController()
        processed_data = command_controller.server_action_commands(input_command, data, file_format, output_file_location)
        return processed_data

    def create_response(self, processed_data):
        # Create a response here
        response = processed_data
        return response
