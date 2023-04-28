from abc import ABCMeta, abstractmethod


class IDatabaseConnector(metaclass=ABCMeta):

    @abstractmethod
    def start_connection(self):
        pass

    @abstractmethod
    def end_connection(self):
        pass
