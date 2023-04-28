class Game:
    def __init__(self, game_type: int | str | None, players: []):
        self.game_type: int | str | None = game_type
        self.players: [] = players

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.game_type == other.game_type and \
                self.players == other.players
        return False
