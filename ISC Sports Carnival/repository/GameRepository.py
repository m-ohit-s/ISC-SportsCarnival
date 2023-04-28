from pypyodbc import Connection
from repository.IGameRepository import IGameRepository


class GameRepository(IGameRepository):

    def insertIntoGame(self, query: str, connection: Connection):
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            print("Successfully Inserted")
        return connection
