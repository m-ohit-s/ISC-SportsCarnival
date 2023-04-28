class TeamQuery:

    @staticmethod
    def insert_in_teams():
        return f"""
                insert into dbo.teams(team_name, game_id) OUTPUT INSERTED.team_id
                values(?, ?)
                """

    @staticmethod
    def get_teams_query():
        return f"""SELECT teams.team_id, teams.team_name, 
                    STRING_AGG(players.player_name, ', ') AS players, 
                    teams.game_id
                    FROM players 
                    INNER JOIN teams_players ON players.player_id = teams_players.player_id
                    INNER JOIN teams ON teams_players.team_id = teams.team_id
                    GROUP BY teams.team_id, teams.game_id, teams.team_name;
                """
