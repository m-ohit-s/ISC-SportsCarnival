import json
import re
import socket
from typing import Match

from communication_protocol.ICSRequest import ICSRequest
from communication_protocol.RequestResponseHandler import RequestResponseHandler
from configurations.Configurator import Configurator
from core.client_server.command_controller.CommandController import CommandController
from core.client_server.isc_client_server.Client import Client
from exceptions.CommandException import CommandException
from model.Protocol import Protocol
from model.ProtocolIpPort import ProtocolIpPort
from utils.custom_logger.CustomLogger import CustomLogger
from utils.json_encoder.ObjectEncoder import ObjectEncoder

configurator = Configurator()
config_data = configurator.load_configurations()
logger = CustomLogger()

pattern = r'isc -a (?P<action>\w+) -i (?P<json_input_file>\'[^\']+\') -o (?P<json_output_file>\'[^\']+\')'
command_controller = CommandController()


def check_command_pattern(regex_pattern: str, command_pattern: str) -> Match[str] | None:
    return re.match(regex_pattern, command_pattern)


def parse_command(command_string):
    match = check_command_pattern(config_data['default_command_pattern'], command_string)
    if not match:
        raise CommandException.InvalidCommand
    action = match.group('action')
    input_file = match.group('input_file')
    output_file = match.group('output_file')

    return action, input_file, output_file


with Client(config_data["hostname"], int(config_data["port"])) as client:
    user_input = input(f"(Enter {config_data['exit_client']} to exit) Enter command: ")
    while user_input != config_data['exit_client']:
        if user_input == config_data["reconnect"]:
            logger.info("reconnecting server")
            client.reconnect_socket(5)
            user_input = input("(Enter quit to exit) Enter command: ")
            continue

        elif user_input == config_data["help_command"]:
            logger.info("help")
            print(f"{config_data['create_team_command']} -> creating team in database\n"
                  f"{config_data['save_team_command']} -> saving team in database\n"
                  f"{config_data['get_team_command']} -> getting team from database\n"
                  f"{config_data['reconnect']} -> reconnecting with the server\n")
            user_input = input("(Enter quit to exit) Enter command: ")
            continue

        try:
            action, input_file, output_file = parse_command(user_input)
            data = command_controller.client_action_commands(action, input_file, output_file)
            logger.info(f"data fetched from file: {data}")

            data_list = [action, None if data is None else data.replace(" ", ""), output_file]
            request: ICSRequest = RequestResponseHandler.create_request(
                1024,
                ProtocolIpPort(config_data["hostname"], int(config_data["port"])),
                ProtocolIpPort(config_data["hostname"], int(config_data["port"])),
                data_list,
                Protocol("1.1", "json"),
                {"source_ip": config_data["hostname"],
                 "source_port": int(config_data["port"]),
                 "destination_ip": config_data["hostname"],
                 "destination_port": int(config_data["port"])}
            )
            logger.debug(f"request object -> {request}")

            data = json.dumps(request, cls=ObjectEncoder)
            response = client.send_data(data)
            if action == "get_team":
                response = json.loads(response)
                team_data = response["data"]
                for row in team_data:
                    print(row)
            user_input = input("(Enter quit to exit) Enter command: ")

        except CommandException.InvalidCommand as e:
            print(e.message)
            logger.warning(f"Invalid Command")
            user_input = input(f"(Enter {config_data['exit_client']} to exit) Enter command: ")

        except FileNotFoundError as f:
            logger.error(f"FileNotFound")
            print("File Path Invalid. Check Again")
            user_input = input(f"(Enter {config_data['exit_client']} to exit) Enter command: ")

        except socket.error:
            logger.error(f"Cannot connect to the server")
            user_input = ""
            continue

    client.send_data(json.dumps({"action": "quit"}))
