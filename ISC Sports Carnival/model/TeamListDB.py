class TeamListDB:
    def __init__(self, teams: list, total: int, additional_players: list):
        self.teams: list = teams
        self.total: int = total
        self.additional_players: list = additional_players