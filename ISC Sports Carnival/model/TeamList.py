import json


class TeamList:
    def __init__(self, teams: list, total: int, additional_players: list):
        self.teams: list = teams
        self.total: int = total
        self.additional_players: list = additional_players

    def __eq__(self, other):
        if isinstance(other, TeamList):
            return self.teams == other.teams and \
                self.total == other.total and \
                self.additional_players == other.additional_players
        return False

    @classmethod
    def from_dict(cls, data):
        data = json.loads(data)
        return cls(data["teams"], data["total"], data["additional_players"])
