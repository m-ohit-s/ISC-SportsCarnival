import os
from configparser import ConfigParser

from core.client_server.command_controller.CommandController import CommandController
from extra_client_server.project_client_server.MainClient import MainClient

config = ConfigParser()
config.read(f"{os.getcwd()}\\configurations\\configurations.ini")
config_data = config["DEFAULT"]

command_controller = CommandController()
data = command_controller.client_action_commands("create_teams", config_data["input_file_location"])
client = MainClient(config_data["hostname"], int(config_data["port"]))
client.connect()

client.send_data(data)
client.receive_data()
