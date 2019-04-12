import numpy as np
import pandas as pandas


class Game(object):
    def __init__(self, rows=8, columns=8):
        self.columns = columns
        self.rows = rows
        self.matrix = np.zeros((self.rows, self.columns), dtype=int)

    def set_alive(self, row, column):
        try:
            self.matrix[row][column] = 1
        except IndexError as error:
            print(error)

    def print(self):
        df = pandas.DataFrame(self.matrix)
        print(df)

    def bounded_cell(self, row, column):
        return 0 <= row < self.rows and 0 <= column < self.columns

    def is_dead_cell(self, row, column):
        return self.matrix[row][column] == 0

    def is_alive_cell(self, row, column):
        return self.matrix[row][column] == 1

    def count_alive_neighbours(self, row, column):
        neighbours = [
            [row - 1, column - 1],
            [row - 1, column],
            [row - 1, column + 1],
            [row, column + 1],
            [row + 1, column + 1],
            [row + 1, column],
            [row + 1, column - 1],
            [row, column - 1]
        ]
        alive_neighbours = 0

        for axe in neighbours:
            next_neighbour_row = axe[0]
            next_neighbour_column = axe[1]
            if self.bounded_cell(next_neighbour_row, next_neighbour_column):
                if self.is_alive_cell(next_neighbour_row, next_neighbour_column):
                    alive_neighbours += 1

        return alive_neighbours

    def is_alive_with_less_than_two_alive_neighbours(self, row, column):
        return self.is_alive_cell(row, column) and self.count_alive_neighbours(row, column) < 2

    def is_alive_with_more_than_three_alive_neighbours(self, row, column):
        return self.is_alive_cell(row, column) and self.count_alive_neighbours(row, column) > 3

    def is_alive_with_two_or_three_alive_neighbours(self, row, column):
        return self.is_alive_cell(row, column) and (self.count_alive_neighbours(row,
                                                                                column) == 2 or self.count_alive_neighbours(
            row, column) == 3)

    def is_dead_with_three_alive_neighbours(self, row, column):
        return self.is_dead_cell(row, column) and self.count_alive_neighbours(row, column) == 3

    def play(self):
        output_matrix = self.matrix.copy()
        for x in range(0, self.rows - 1):
            for y in range(0, self.columns - 1):
                if self.is_alive_with_less_than_two_alive_neighbours(x, y):
                    output_matrix[x][y] = 0
                if self.is_alive_with_more_than_three_alive_neighbours(x, y):
                    output_matrix[x][y] = 0
                if self.is_alive_with_two_or_three_alive_neighbours(x, y):
                    output_matrix[x][y] = 1
                if self.is_dead_with_three_alive_neighbours(x, y):
                    output_matrix[x][y] = 1

        self.matrix = output_matrix.copy()


if __name__ == '__main__':
    game_instance = Game(4, 8)
    game_instance.set_alive(1, 5)
    game_instance.set_alive(2, 4)
    game_instance.set_alive(2, 5)
    game_instance.print()
    game_instance.play()
    print("------------------------------------------")
    game_instance.print()
