from pypyodbc import Connection

from core.database.queries.TeamPlayerQuery import TeamPlayerQuery
from model.TeamPlayerDB import TeamPlayerDB
from repository.ITeamPlayerRepository import ITeamPlayerRepository


class TeamPlayerRepository(ITeamPlayerRepository):

    def insertIntoTeamPlayer(self, team_player: TeamPlayerDB, connection: Connection):
        with connection.cursor() as cursor:
            cursor.execute(TeamPlayerQuery().insert_in_team_player(), (team_player.player_id, team_player.team_id))
            connection.commit()
            print("Successfully Inserted")
        return connection
