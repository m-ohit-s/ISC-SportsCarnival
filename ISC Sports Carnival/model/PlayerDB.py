class PlayerDB:
    def __init__(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name

    @classmethod
    def from_dict(cls, data):
        return cls(data['player_id'], data['player_name'])
