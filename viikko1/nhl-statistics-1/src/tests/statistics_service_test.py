import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("wsimerkki1", "1", 4, 12),
            Player("esimerkki2", "2", 45, 54),
            Player("esimerrki3",   "1", 37, 53),
            Player("esimerkki4", "DET", 42, 56),   
            Player("esimerkki5", "1", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
       
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_correct_name(self):
        player = self.stats.search("esimerkki5")
        self.assertEqual(player.name, "esimerkki5")

    def test_wrong_search_returns_none(self):
        player = self.stats.search("Gretski")
        self.assertEqual(player, None)

    def test_team_returns_correct_players(self):
        players_of_1 = self.stats.team("1")
        self.assertEqual(len(players_of_1), 3) # len = 3

        players_of_2 = self.stats.team("2")
        self.assertEqual(len(players_of_2), 1) # len = 1

    def test_top_points_correct(self):
        top_scorers = self.stats.top(2)
        self.assertEqual(top_scorers[0].name, "esimerkki5")
        self.assertEqual(top_scorers[1].name, "esimerkki2")

    
        top_scorers = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(top_scorers[0].name, "esimerkki5")
        self.assertEqual(top_scorers[1].name, "esimerkki2")

    def test_top_goals_correct(self):
        top_goal_scorers = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(top_goal_scorers[0].name, "esimerkki2")
        self.assertEqual(top_goal_scorers[1].name, "esimerkki4")

    def test_top_assists_correct(self):
        top_assists = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(top_assists[0].name, "esimerkki5")
        self.assertEqual(top_assists[1].name, "esimerkki4")

    def test_top_with_wrong_(self):
        top_nothings = self.stats.top(2, 7)
        self.assertIsNone(top_nothings)