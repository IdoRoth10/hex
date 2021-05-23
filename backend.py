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
        if player == 1:
            is_win = False
            for i in range(0, self.n):
                if self.board[i][0] == 1:
                    is_win = is_win or self.checkWinP1(i, 0)
            return is_win

        else:
            # return self.checkWinP2(self.board, 0)
            pass


    def checkWinP1(self, i, j):
        """
            p1 - blue player
            from col = 0 to col = self.n - 1
            -1 is a visited spot
        """
        if i >= self.n or i < 0 or j >= self.n or j < 0 or self.board[i][j] != 1:
            return False
        if j == self.n-1:
            return True

        self.board[i][j] = -1
        result = self.checkWinP1(i - 1, j) or self.checkWinP1(i - 1, j+1) or self.checkWinP1(i, j - 1) or\
                 self.checkWinP1(i, j + 1) or self.checkWinP1(i + 1, j - 1) or self.checkWinP1(i + 1, j)
        self.board[i][j] = 1
        return result


    def chekWinP2(self, board, i):
        pass


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
