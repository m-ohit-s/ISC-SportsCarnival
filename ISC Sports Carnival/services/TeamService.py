from pypyodbc import Connection
from exceptions import CreateTeamExceptions
from model.Error import Error
from model.Player import Player
from model.Game import Game
from model.PlayerDB import PlayerDB
from model.Team import Team
from model.TeamList import TeamList
from model.TeamListDB import TeamListDB
from model.TeamPlayerDB import TeamPlayerDB
from repository.PlayerRepository import PlayerRepository
from repository.TeamRepository import TeamRepository
from services.GameService import GameService
from services.ITeamService import ITeamService
from repository.TeamPlayerRepository import TeamPlayerRepository


class TeamService(ITeamService):

    def __init__(self):
        self.__team_id = 0
        self.__team_name = "Team-"
        self.__team_suffix = 64
        self.__single_team = []
        self.__team_list = []
        self.__counter = 1
        self.__game_service = GameService()
        self.__team_repository = TeamRepository()
        self.__player_repository = PlayerRepository()
        self.__team_player_repository = TeamPlayerRepository()

    def create_teams(self, game: Game):
        try:
            if not self.__is_player_count_valid(game):
                raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(description="Total number of players are "
                                                                                        "less for team creation.",
                                                                            error_code=11)
            else:
                number_of_players_needed = self.__fetch_total_players_needed(game)
                number_of_players_registered = self.__fetch_total_players_registered(game)
                additional_players = []
                team_counter = 0
                for player in game.players:
                    self.__validate_player_data_boundary_conditions(player)
                    if self.__counter == number_of_players_needed:
                        self.__counter = 1
                        self.__single_team.append(player)
                        team_object = self.__create_team_object(self.__single_team, game)
                        self.__add_team(team_object)
                        team_counter += 1
                        self.__single_team = []
                    else:
                        if team_counter >= number_of_players_registered // number_of_players_needed:
                            additional_players.append(player)
                        else:
                            self.__single_team.append(player)
                            self.__counter += 1
                return TeamList(self.__team_list, len(self.__team_list), additional_players)

        except CreateTeamExceptions.CreateTeamExceptions.InvalidData as e:
            return Error(e.error_type, e.message, e.description)

    def save_teams(self, teams: TeamList, connection: Connection):
        team_db = self.__convert_team_obj_to_team_db_obj(teams)
        for team in team_db.teams:
            temp_team = Team.from_dict(team)
            team_id = self.__team_repository.insertIntoTeam(temp_team, connection)
            for player in temp_team.players:
                temp_player = PlayerDB.from_dict(player)
                player_id = self.__player_repository.insertIntoPlayer(temp_player, connection)
                team_player_db = TeamPlayerDB(player_id, team_id)
                self.__team_player_repository.insertIntoTeamPlayer(team_player_db, connection)
        for player in team_db.additional_players:
            temp_player = PlayerDB.from_dict(player)
            self.__player_repository.insertIntoPlayer(temp_player, connection)

    def get_teams(self, connection):
        return self.__team_repository.getTeams(connection)

    def __is_player_count_valid(self, game) -> bool:
        number_of_players_needed = self.__fetch_total_players_needed(game)
        total_players_registered = self.__fetch_total_players_registered(game)
        try:
            if total_players_registered / number_of_players_needed >= 1:
                return True
            else:
                return False
        except ZeroDivisionError:
            raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(description="Invalid Game Type",
                                                                        error_code=12)

    def __fetch_total_players_needed(self, game: Game):
        return self.__game_service.get_players_required_in_a_team(game.game_type)

    def __fetch_total_players_registered(self, game: Game) -> int:
        if game.players is None:
            return 0
        return self.__game_service.get_participants_count(game.players)

    def __create_team_object(self, team, game: Game):
        self.__team_id += 1
        self.__team_suffix = self.__team_suffix + 1
        return Team(self.__team_id, (self.__team_name + chr(self.__team_suffix)), game.game_type, team)

    def __add_team(self, team_object: Team):
        self.__team_list.append(team_object)

    @staticmethod
    def __convert_team_obj_to_team_db_obj(teams: TeamList):
        return TeamListDB(teams.teams, teams.total, teams.additional_players)

    @staticmethod
    def __validate_player_data_boundary_conditions(player: Player):
        if type(player.player_id) == str:
            raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(message="Incorrect Data Format",
                                                                        description="Player id can not be "
                                                                                    "in string",
                                                                        error_code=21)
        elif player.player_name == "":
            raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(message="Incorrect Data Format",
                                                                        description="Player name can not be "
                                                                                    "empty",
                                                                        error_code=22)

        elif player.player_id is None:
            raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(message="Incorrect Data Format",
                                                                        description="Player id can not be "
                                                                                    "null",
                                                                        error_code=23)

        elif player.player_name is None:
            raise CreateTeamExceptions.CreateTeamExceptions.InvalidData(message="Incorrect Data Format",
                                                                        description="Player name can not be "
                                                                                    "null",
                                                                        error_code=24)
