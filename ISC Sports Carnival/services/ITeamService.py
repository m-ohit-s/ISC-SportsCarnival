from abc import ABCMeta, abstractmethod

from pypyodbc import Connection

from model import TeamDB
from model.Game import Game


class ITeamService(metaclass=ABCMeta):

    @abstractmethod
    def create_teams(self, game: Game):
        pass

    @abstractmethod
    def save_teams(self, team: TeamDB, connection: Connection):
        pass

    @abstractmethod
    def get_teams(self, connection: Connection):
        pass
