from pypyodbc import Connection

from core.database.queries.PlayerQuery import PlayerQuery
from model.PlayerDB import PlayerDB
from repository.IPlayerRepository import IPlayerRepository


class PlayerRepository(IPlayerRepository):

    def insertIntoPlayer(self, player: PlayerDB, connection: Connection):
        with connection.cursor() as cursor:
            player_id = cursor.execute(PlayerQuery.insert_in_players(), (player.player_name,)).fetchone()[0]
            connection.commit()
            print("Successfully Inserted")
            return player_id
