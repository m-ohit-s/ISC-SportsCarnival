from pypyodbc import Connection

from core.database.queries.TeamQuery import TeamQuery
from model.TeamDB import TeamDB
from repository.ITeamRepository import ITeamRepository


class TeamRepository(ITeamRepository):

    def insertIntoTeam(self, team: TeamDB, connection: Connection):
        with connection.cursor() as cursor:
            team_id = cursor.execute(TeamQuery.insert_in_teams(), (team.team_name, team.game_type)).fetchone()[0]
            connection.commit()
            print("Successfully Inserted")
            return team_id

    def getTeams(self, connection: Connection):
        with connection.cursor() as cursor:
            cursor.execute(TeamQuery.get_teams_query())
            results = cursor.fetchall()
            print(results)
            for row in results:
                print(row)
            return results
