import unittest
from src.allTheFunctions import already_been_there
from src.Cplayer import player

class TestATF(unittest.TestCase):

    def test_alreadyBeenThere(self):
        mock_player = player(1, 2, 5, 0, 30, 30, 60, 60, 0, 100, [], [], [], 0, [])
        mock_player.alreadyBeenHere.append([0, 1])
        mock_player.alreadyBeenHere.append([0, 2])
        mock_player.alreadyBeenHere.append([0, 3])
        self.assertTrue(already_been_there(mock_player, [0,1]))

if __name__ == '__main__':
    unittest.main()