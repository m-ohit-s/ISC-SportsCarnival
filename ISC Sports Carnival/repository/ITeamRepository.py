from abc import ABCMeta, abstractmethod

from pypyodbc import Connection


class ITeamRepository(metaclass=ABCMeta):

    @abstractmethod
    def insertIntoTeam(self, query: str, connection: Connection):
        pass
