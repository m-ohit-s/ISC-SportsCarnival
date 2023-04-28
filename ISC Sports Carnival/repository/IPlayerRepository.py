from abc import ABCMeta, abstractmethod

from pypyodbc import Connection

from model.PlayerDB import PlayerDB


class IPlayerRepository(metaclass=ABCMeta):

    @abstractmethod
    def insertIntoPlayer(self, player: PlayerDB, connection: Connection):
        pass
