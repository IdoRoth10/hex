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


    def chekWin(self, player):
        if player == 1:
            is_win = False
            for i in range(0, self.n):
                if self.board[i][0] == 1:
                    is_win = is_win or self.checkWinP1(i, 0)
            return is_win

        else:
            is_win = False
            for j in range(0, self.n):
                if self.board[0][j] == 2:
                    is_win = is_win or self.checkWinP2(0, j)
            return is_win


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

    def checkWinP2(self, i, j):
        """
                    p2 - red player
                    from roe = 0 to row = self.n - 1
                    -1 is a visited spot
                """
        if j >= self.n or j < 0 or i >= self.n or i < 0 or self.board[i][j] != 2:
            return False
        if i == self.n - 1:
            return True

        self.board[i][j] = -1
        result = self.checkWinP2(i - 1, j) or self.checkWinP2(i - 1, j + 1) or self.checkWinP2(i, j - 1) or \
                 self.checkWinP2(i, j + 1) or self.checkWinP2(i + 1, j - 1) or self.checkWinP2(i + 1, j)
        self.board[i][j] = 2
        return result

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
    b.chekWin(1)
    print(b)
