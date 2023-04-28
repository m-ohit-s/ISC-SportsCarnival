import pypyodbc
from core.database.IDatabaseConnector import IDatabaseConnector
from exceptions.DatabaseExceptions import DatabaseExceptions
from utils.custom_logger.CustomLogger import CustomLogger


class DatabaseConnector(IDatabaseConnector):
    __instance = None

    @staticmethod
    def get_instance(connection_string):
        if DatabaseConnector.__instance is None:
            DatabaseConnector(connection_string)
        return DatabaseConnector.__instance

    def __init__(self, connection_string):
        self.logger = CustomLogger()
        self.connection_string = connection_string
        if DatabaseConnector.__instance is not None:
            raise DatabaseExceptions.SingletonInstanceException
        else:
            self.connection = self.start_connection()
            DatabaseConnector.__instance = self

    def start_connection(self):
        self.logger.info("starting database connection")
        return pypyodbc.connect(self.connection_string)

    def end_connection(self):
        self.logger.info("starting database connection")
        return self.connection.close()
