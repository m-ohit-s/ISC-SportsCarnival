from abc import ABCMeta, abstractmethod

from pypyodbc import Connection

from model.Team import Team


class IAdminService(metaclass=ABCMeta):

    @abstractmethod
    def create_teams(self, input_location: str, file_format: str):
        pass

    @abstractmethod
    def save_teams(self, team: Team, connection: Connection):
        pass

    @abstractmethod
    def get_teams(self, connection: Connection):
        pass
