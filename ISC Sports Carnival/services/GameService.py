from exceptions import CreateTeamExceptions
from model.Player import Player
from utils.rules.RequiredPlayer import RequiredPlayer
from core.enums.GameType import GameType
from model.Game import Game
from services.IGameService import IGameService


class GameService(IGameService):

    def get_players_required_in_a_team(self, game_id: int) -> int:
        try:
            if game_id not in [item.value for item in GameType]:
                raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(description="Invalid Game Type")
        except CreateTeamExceptions.CreateTeamExceptions.InvalidData:
            return 0
        game_name = GameType(game_id)
        required_player = RequiredPlayer()
        return required_player.getNumberOfRequiredPlayers(game_name)

    def get_participants_count(self, participantsList: list) -> int:
        return len(participantsList)

    def create_game_data_object(self, data: dict) -> Game:
        return self.__create_game_data_based_on_input(data)

    def __create_game_data_based_on_input(self, data: dict) -> Game | None:
        players = []
        if (data.get("players") is None) and (data.get("gameType") is None):
            return None
        elif (data.get("players") is None) and (data.get("gameType") is not None):
            return None
        elif (data.get("players") is not None) and (data.get("gameType") is None):
            return None
        elif (data.get("players") is not None) and (data.get("gameType") is not None):
            for _data in data["players"]:
                players.append(Player.from_dict(_data))
            return Game(data['gameType'], players)
        return Game(data['gameType'], data['players'])
