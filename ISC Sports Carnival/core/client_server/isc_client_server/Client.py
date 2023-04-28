import json
import socket
import time

from configurations.Configurator import Configurator
from utils.custom_logger.CustomLogger import CustomLogger


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.logger = CustomLogger()
        self.config_data = Configurator().load_configurations()

    def __enter__(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.logger.info(f"connecting to server ...")
            print(f"Connected to {self.host}:{self.port}")
        except ConnectionRefusedError as e:
            self.logger.error(f"{e}")
            print(f"something went wrong with server. Try Again after sometime or Try running"
                  f" {self.config_data['reconnect']} command")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        self.logger.info(f"closing socket connection ...")
        self.socket = None

    def send_data(self, data):
        try:
            self.socket.sendall(data.encode())
            return self.socket.recv(1024).decode()
        except socket.error:
            self.logger.critical(f"socket connection ended ...")
            print(f"unable to send request to server. Try reconnecting with the server again using"
                  f"{self.config_data['reconnect']} to reconnect")

    def close(self):
        self.logger.info("closing connection")
        self.socket.sendall(json.dumps({"action": "quit"}).encode())
        self.socket.close()

    def reconnect_socket(self, attempts):
        self.logger.info(f"attempting to reconnect...")
        reconnect_count = 0
        while True:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                self.logger.info(f"Socket reconnected")
                print("Socket reconnected")
                break
            except socket.error as e:
                self.logger.critical(f"{e}")
                if reconnect_count < attempts:
                    print("Error reconnecting socket: Trying Again")
                    reconnect_count += 1
                    print(f"attempted {reconnect_count} time...")
                    time.sleep(5)
                else:
                    print(f"Attempted {attempts} times. Try requesting after some time.")
                    self.logger.info(f"Attempted {attempts} times. Try requesting after some time.")
                    break
