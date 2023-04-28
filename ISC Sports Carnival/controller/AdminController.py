from model.TeamList import TeamList
from services.AdminService import AdminService
from pypyodbc import Connection

from utils.custom_logger.CustomLogger import CustomLogger


class AdminController:

    def __init__(self):
        self.adminService = AdminService()
        self.logger = CustomLogger()

    def create_teams(self, data, file_format):
        self.logger.debug("calling create teams")
        return self.adminService.create_teams(data, file_format)

    def save_teams(self, teams: TeamList, connection: Connection):
        self.logger.debug("calling save teams")
        return self.adminService.save_teams(teams, connection)

    def get_teams(self, connection: Connection):
        self.logger.debug("calling get teams")
        return self.adminService.get_teams(connection)
