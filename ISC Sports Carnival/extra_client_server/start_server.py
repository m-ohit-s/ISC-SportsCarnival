import os
from configparser import ConfigParser

from extra_client_server.multi_threaded.MultiThreadedServer import MultiThreadedServer

config = ConfigParser()
config.read(f"{os.getcwd()}\\configurations\\configurations.ini")
config_data = config["DEFAULT"]

server = MultiThreadedServer(config_data["hostname"], int(config_data["port"]), config_data["size"], config_data["format"], config_data["disconnect_msg"])

server.start_connection()

