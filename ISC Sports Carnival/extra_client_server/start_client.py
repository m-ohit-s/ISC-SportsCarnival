import os
from configparser import ConfigParser

from extra_client_server.multi_threaded.MultiThreadedClient import MultiThreadedClient

config = ConfigParser()
config.read(f"{os.getcwd()}\\configurations\\configurations.ini")
config_data = config["DEFAULT"]

client = MultiThreadedClient(config_data["hostname"], int(config_data["port"]), config_data["size"], config_data["format"],
                    config_data["disconnect_msg"])

client.connect_server()

message = input("> ")
message = client.start_communication(message, config_data["disconnect_msg"])

client.disconnect_server()
