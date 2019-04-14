from unittest import TestCase
import Game as GameModule


class GameUnitTest(TestCase):

    def setUp(self):
        self.game_instance = GameModule.Game(4, 8)

    def test_with_no_alive_neighbour(self):
        neighbours_count = self.game_instance.count_alive_neighbours(1, 4)
        self.assertEqual(0, neighbours_count)

    def test_with_one_alive_neighbour(self):
        self.game_instance.set_alive(0, 3)
        neighbours_count = self.game_instance.count_alive_neighbours(1, 4)
        self.assertEqual(1, neighbours_count)

    def test_with_two_alive_neighbours(self):
        self.game_instance.set_alive(0, 3)
        self.game_instance.set_alive(0, 4)
        neighbours_count = self.game_instance.count_alive_neighbours(1, 4)
        self.assertEqual(2, neighbours_count)

    def test_with_three_alive_neighbours(self):
        self.game_instance.set_alive(0, 3)
        self.game_instance.set_alive(0, 4)
        self.game_instance.set_alive(0, 5)
        neighbours_count = self.game_instance.count_alive_neighbours(1, 4)
        self.assertEqual(3, neighbours_count)

    def test_with_fewer_than_two_dead_neighbour(self):
        self.game_instance.set_alive(0, 0)
        self.game_instance.set_alive(0, 1)
        self.game_instance.play()
        self.assertTrue(self.game_instance.is_dead_cell(0, 0))

    def test_dead_cell_get_alive_with_three_alive_neighbours(self):
        self.game_instance.set_alive(0, 3)
        self.game_instance.set_alive(0, 4)
        self.game_instance.set_alive(0, 5)
        self.game_instance.play()
        self.assertTrue(self.game_instance.is_alive_cell(1, 4))
