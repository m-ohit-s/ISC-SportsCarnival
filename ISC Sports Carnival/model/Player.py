class Player:
    def __init__(self, player_id: int | str | None, player_name: str | None):
        self.player_id: int | str | None = player_id
        self.player_name: str | None = player_name

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.player_id == other.player_id and \
                self.player_name == other.player_name
        return False

    @classmethod
    def from_dict(cls, data):
        return cls(data['playerId'], data['name'])
