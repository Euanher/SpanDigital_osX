import unittest
from main import parse_input, calculate_points, rank_teams, format_output

class TestLeagueRanking(unittest.TestCase):

    def test_parse_input(self):
        input_lines = ["Lions 3, Snakes 3", "Tarantulas 1, FC Awesome 0"]
        expected = [
            ("Lions", 3, "Snakes", 3),
            ("Tarantulas", 1, "FC Awesome", 0),
        ]
        self.assertEqual(parse_input(input_lines), expected)

    def test_calculate_points(self):
        results = [
            ("Lions", 3, "Snakes", 3),
            ("Tarantulas", 1, "FC Awesome", 0),
        ]
        expected = {
            "Lions": 1,
            "Snakes": 1,
            "Tarantulas": 3,
            "FC Awesome": 0,
        }
        self.assertEqual(calculate_points(results), expected)

    def test_rank_teams(self):
        points = {
            "Lions": 5,
            "Snakes": 1,
            "Tarantulas": 6,
            "FC Awesome": 1,
            "Grouches": 0,
        }
        expected = [
            (1, "Tarantulas", 6),
            (2, "Lions", 5),
            (3, "FC Awesome", 1),
            (3, "Snakes", 1),
            (5, "Grouches", 0),
        ]
        self.assertEqual(rank_teams(points), expected)

    def test_format_output(self):
        rankings = [
            (1, "Tarantulas", 6),
            (2, "Lions", 5),
            (3, "FC Awesome", 1),
            (3, "Snakes", 1),
            (5, "Grouches", 0),
        ]
        expected_output = """\
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts"""
        self.assertEqual(format_output(rankings), expected_output)

if __name__ == "__main__":
    unittest.main()
