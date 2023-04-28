from core.enums.GameType import GameType


class RequiredPlayer:

    def __init__(self):
        self.__sports = {
            GameType.cricket: 11,
            GameType.badminton_doubles: 2,
            GameType.chess: 1,
        }

    def getNumberOfRequiredPlayers(self, sport: GameType) -> int:
        return self.__sports[sport]
