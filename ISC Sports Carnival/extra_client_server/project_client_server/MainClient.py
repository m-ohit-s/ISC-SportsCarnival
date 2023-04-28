import socket
import time
from utils.custom_logger.CustomLogger import CustomLogger


class MainClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.reconnect_count = 0

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")

        except ConnectionRefusedError as e:
            print(f"something went wrong with server. Try Again after sometime")

    def send_data(self, data):
        try:
            self.socket.send(data.encode())
        except socket.error as e:
            print("Error sending data:", e)
            self.reconnect_socket()

    def receive_data(self):
        return self.socket.recv(1024).decode()

    def close(self):
        try:
            self.socket.close()
        except socket.error as e:
            print(f"Error in closing connection: {e}")

    def reconnect_socket(self):
        while True:
            try:
                self.socket.connect((self.host, self.port))
                print("Socket reconnected")
                break
            except socket.error as e:
                if self.reconnect_count >= 5:
                    print("Error reconnecting socket: Trying Again")
                    self.reconnect_count += 1
                    time.sleep(1)
                else:
                    print("Attempted 5 times. Try requesting after some time.")
                    break
