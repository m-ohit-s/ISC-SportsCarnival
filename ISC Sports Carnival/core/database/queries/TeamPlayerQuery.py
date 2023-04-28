from model import TeamPlayerDB


class TeamPlayerQuery:

    @staticmethod
    def insert_in_team_player():
        return f"""
                insert into dbo.teams_players(player_id, team_id)
                values(?, ?)
                """
