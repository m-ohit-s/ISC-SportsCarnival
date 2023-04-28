from pypyodbc import Connection

from core.data_operations.input_output_data.InputData import InputData
from exceptions import CreateTeamExceptions
from model.Error import Error
from model.Team import Team
from model.TeamList import TeamList
from services.GameService import GameService
from services.IAdminService import IAdminService
from services.TeamService import TeamService
from utils.custom_logger.CustomLogger import CustomLogger


class AdminService(IAdminService):

    def __init__(self):
        self.team_service = TeamService()
        self.game_service = GameService()

    def create_teams(self, data, file_format: str):
        input_data = InputData()
        data = input_data.process_data(data, file_format)
        try:
            game_data = self.game_service.create_game_data_object(data)
            if game_data is None:
                raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(description="Missing Fields in Input -> "
                                                                                        "GameType | Players")
            return self.team_service.create_teams(game_data)
        except CreateTeamExceptions.CreateTeamExceptions.InvalidData as e:
            return Error(e.error_type, e.message, e.description)

    def save_teams(self, teams: TeamList, connection: Connection):
        return self.team_service.save_teams(teams, connection)

    def get_teams(self, connection: Connection):
        return self.team_service.get_teams(connection)
