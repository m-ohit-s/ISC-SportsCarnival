from abc import ABCMeta, abstractmethod

from pypyodbc import Connection


class ITeamPlayerRepository(metaclass=ABCMeta):

    @abstractmethod
    def insertIntoTeamPlayer(self, query: str, connection: Connection):
        pass
