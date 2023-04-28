from core.commands.Command import CreateTeamCommand, SaveTeamCommand, GetTeamCommand
from exceptions.CommandException import CommandException


class CommandController:

    @staticmethod
    def server_action_commands(input_command, data, file_format, output_file):
        if input_command == "create_team":
            create_team_command = CreateTeamCommand(data=data, file_format=file_format, output_file=output_file)
            return create_team_command.execute_server()

        if input_command == "save_team":
            save_team_command = SaveTeamCommand(data=data)
            return save_team_command.execute_server()

        if input_command == "get_team":
            get_team_command = GetTeamCommand()
            return get_team_command.execute_server()

    @staticmethod
    def client_action_commands(input_command, input_file="", output_file=""):
        if input_command == "create_team":
            create_team_command = CreateTeamCommand(input_file, output_file)
            return create_team_command.execute_client()

        elif input_command == "save_team":
            save_team_command = SaveTeamCommand(input_file)
            return save_team_command.execute_client()

        elif input_command == "get_team":
            get_team_command = GetTeamCommand()
            return get_team_command.execute_client()

        else:
            print("No such action exist check command again.")
            raise CommandException.InvalidCommand
