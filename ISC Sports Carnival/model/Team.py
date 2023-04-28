class Team:
    def __init__(self, team_id, team_name, game_type, players):
        self.team_id = team_id
        self.team_name = team_name
        self.game_type = game_type
        self.players = players

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.team_id == other.team_id and \
                self.team_name == other.team_name and \
                self.game_type == other.game_type and \
                self.players == other.players
        return False

    @classmethod
    def from_dict(cls, data):
        return cls(data["team_id"], data["team_name"], data["game_type"], data["players"])
