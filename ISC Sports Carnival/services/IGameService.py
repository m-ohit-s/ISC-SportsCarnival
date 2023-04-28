from abc import ABCMeta, abstractmethod

from factory.DataFactory import DataFactory
from model.Game import Game


class IGameService(metaclass=ABCMeta):

    @abstractmethod
    def get_players_required_in_a_team(self, gameID: int) -> int:
        pass

    @abstractmethod
    def get_participants_count(self, participantsList: list) -> int:
        pass

    @abstractmethod
    def create_game_data_object(self, data) -> Game:
        pass
