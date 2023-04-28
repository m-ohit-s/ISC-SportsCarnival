import os
from configparser import ConfigParser
from extra_client_server.test.TeamServer import TeamServer

config = ConfigParser()
config.read(f"{os.getcwd()}\\configurations\\configurations.ini")
config_data = config["DEFAULT"]

server = TeamServer(config_data["hostname"], int(config_data["port"]))

server.start("create_teams", "json", config_data["output_file_location"])
