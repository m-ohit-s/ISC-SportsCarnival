from abc import ABCMeta, abstractmethod

from pypyodbc import Connection


class IGameRepository(metaclass=ABCMeta):

    @abstractmethod
    def insertIntoGame(self, query: str, connection: Connection):
        pass
