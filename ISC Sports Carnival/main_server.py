import os
from configparser import ConfigParser

from core.client_server.isc_client_server.Server import Server
from utils.custom_logger.CustomLogger import CustomLogger

config = ConfigParser()
config.read(f"{os.getcwd()}\\configurations\\configurations.ini")
config_data = config["DEFAULT"]
logger = CustomLogger()

server = Server(config_data["hostname"], int(config_data["port"]))
logger.debug("starting server")
server.start()

