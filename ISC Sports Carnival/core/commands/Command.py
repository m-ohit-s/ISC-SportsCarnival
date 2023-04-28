from configparser import ConfigParser

from configurations.Configurator import Configurator
from controller.AdminController import AdminController
from core.data_operations.input_output_data.InputData import InputData
from core.data_operations.input_output_data.OutputData import OutputData
from core.database.DatabaseConnector import DatabaseConnector
from model.TeamList import TeamList

configurator = Configurator()
config_data = configurator.load_configurations()


class Command:
    def __init__(self, input_file=None, output_file=None, file_format=None, data=None):
        self.input_file = input_file
        self.output_file = output_file
        self.file_format = file_format
        self.data = data

    def execute_client(self):
        pass

    def execute_server(self):
        pass

    def create_database_connection_string(self, driver_name, server_name, database_name):
        return f"""DRIVER={{{driver_name}}};
                    SERVER={server_name};
                    DATABASE={database_name};
                    Trust_Connection=yes;
                """


class CreateTeamCommand(Command):
    def execute_client(self):
        print("Executing create_team command with input file:", self.input_file, "and output file:", self.output_file)
        input_data = InputData()
        data = input_data.read_file(input_data.get_file_object(self.input_file))
        if self.output_file is None:
            raise FileNotFoundError
        if data is None:
            raise FileNotFoundError
        return data

    def execute_server(self):
        admin_controller = AdminController()
        team_data = admin_controller.create_teams(self.data, self.file_format)
        output_data = OutputData()
        output_data.write_data(self.output_file, self.file_format, team_data)
        return team_data


class SaveTeamCommand(Command):
    def execute_client(self):
        print("Executing save_team command with input file:", self.input_file)
        input_data = InputData()
        data = input_data.read_file(input_data.get_file_object(self.input_file))
        try:
            if data is None:
                raise FileNotFoundError
        except FileNotFoundError:
            return data
        return data

    def execute_server(self):
        admin_controller = AdminController()
        database_connector = DatabaseConnector.get_instance(
            self.create_database_connection_string(
                config_data["sql_database_driver_name"],
                config_data["server_name"],
                config_data["database_name"]
            )
        )
        data_obj = TeamList.from_dict(self.data)
        admin_controller.save_teams(data_obj, database_connector.start_connection())
        return data_obj


class GetTeamCommand(Command):
    def execute_client(self):
        print("Executing get_team command")
        return None

    def execute_server(self):
        admin_controller = AdminController()
        database_connector = DatabaseConnector.get_instance(
            self.create_database_connection_string(
                config_data["sql_database_driver_name"],
                config_data["server_name"],
                config_data["database_name"]
            )
        )
        return admin_controller.get_teams(database_connector.start_connection())

