import unittest

from model.Error import Error
from model.Game import Game
from model.Player import Player
from model.Team import Team
from model.TeamList import TeamList
from services.TeamService import TeamService


class CreateTeamTests(unittest.TestCase):

    def test_create_team_logic(self):
        team_service = TeamService()
        game = Game(
            3,
            [Player(1, "A"), Player(2, "B")]
        )
        expected_output = TeamList(
            [Team(1, "Team-A", 3, [Player(1, "A")]),
             Team(2, "Team-B", 3, [Player(2, "B")])],
            2,
            [])
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_additional_players(self):
        team_service = TeamService()
        game = Game(
            2,
            [Player(1, "A"), Player(2, "B"), Player(3, "C"), Player(4, "D"), Player(5, "E")]
        )
        expected_output = TeamList(
            [Team(1, "Team-A", 2, [Player(1, "A"), Player(2, "B")]),
             Team(2, "Team-B", 2, [Player(3, "C"), Player(4, "D")])],
            2,
            [Player(5, "E")])
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_less_player(self):
        team_service = TeamService()
        game = Game(
            3,
            []
        )

        expected_output = Error("Error", "Invalid Data", "Total number of players are less for team creation.")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_string_player_id(self):
        team_service = TeamService()
        game = Game(
            2,
            [Player(1, "A"), Player(2, "B"), Player("3", "C"), Player(4, "D"), Player(5, "E")]
        )
        expected_output = Error("Error", "Incorrect Data Format", "Player id can not be in string")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_empty_player_name(self):
        team_service = TeamService()
        game = Game(
            2,
            [Player(1, "A"), Player(2, "B"), Player(3, "C"), Player(4, ""), Player(5, "E")]
        )
        expected_output = Error("Error", "Incorrect Data Format", "Player name can not be empty")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_null_player_id(self):
        team_service = TeamService()
        game = Game(
            2,
            [Player(1, "A"), Player(2, "B"), Player(3, "C"), Player(None, "D"), Player(5, "E")]
        )
        expected_output = Error("Error", "Incorrect Data Format", "Player id can not be null")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_null_player_name(self):
        team_service = TeamService()
        game = Game(
            2,
            [Player(1, "A"), Player(2, "B"), Player(3, "C"), Player(4, None), Player(5, "E")]
        )
        expected_output = Error("Error", "Incorrect Data Format", "Player name can not be null")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_null_game_type(self):
        team_service = TeamService()
        game = Game(
            None,
            [Player(1, "A"), Player(2, "B"), Player(3, "C"), Player(4, "D"), Player(5, "E")]
        )
        expected_output = Error("Error", "Invalid Data", "Invalid Game Type")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

    def test_create_team_with_null_players(self):
        team_service = TeamService()
        game = Game(
            2,
            None
        )
        expected_output = Error("Error", "Invalid Data", "Total number of players are less for team creation.")
        output = team_service.create_teams(game)
        return self.assertEqual(expected_output, output)

