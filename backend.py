import numpy as np
import sys


class Board:

    def __init__(self):
        """
            0 repesnt empty
            1 repesnt blue
            2 repesnt red
        """
        self.n = 11
        self.board = np.zeros((self.n, self.n), dtype=int)

    def get_value(self, i, j):
        return self.board[i][j]

    def set_value(self, i, j, num):
        self.board[i][j] = num

    def get_neighbors(self, i, j):
        neighbors_list = [(i - 1, j), (i - 1, j+1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i, j + 1)]
        valid_neighbors_list = list()
        for tup in neighbors_list:
            if self.valid_index(tup[0], tup[1]):
                valid_neighbors_list.append(tup)
        return valid_neighbors_list

    def valid_index(self, i, j):
        if i >= self.n or j >= self.n or i<0 or j<0:
            return False
        else:
            return True

    def get_neighbors_same_color(self, i, j, player):
        neighbors_list = self.get_neighbors(i, j)
        color_neighbors = list()
        for tup in neighbors_list:
            if self.get_value(tup[0], tup[1]) == player:
                color_neighbors.append(tup)
        return color_neighbors

    def chekWin(self, player):
        i, j = 0, 0
        if i == 11:
            return False
        if j == 11:
            return False
        return self.get_neighbors(i, j + 1) or self.get_neighbors(i + 1, j)

    def __repr__(self):
        s = ''
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                s += str(self.get_value(i, j))
                s += ' '
            s += ' \n'
        return s


if __name__ == "__main__":
    b = Board()

    print(b)
