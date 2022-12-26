# https://leetcode.com/problems/n-queens/

from david import *
from itertools import chain, product
from functools import cache
from typing import *
import copy

QUEEN = "Q"


def format(board):
    def row_format(row):
        return "".join(i if i is not None else "." for i in row)

    return "\n".join(map(row_format, board))

def _find_boards(n):
    board = [[None] * n for i in range(n)]
    cols = set(range(n))
    diagonals = list(range(0, 2*n-1))
    antidiagonals = list(range(-n+1, n))

    def dfs(r, c):
        """
        attempt to place a queen at r, c
        """
        cols.remove(c)
        diagonals[r+c] = False
        antidiagonals[r-c] = False

        board[r][c] = QUEEN

        if not cols:
            yield format(board)
        else:
            R = r + 1
            # for R, C in product(rows, cols):
            for C in cols:
                if diagonals[R+C] and antidiagonals[R-C]:
                    yield from dfs(R, C)

        board[r][c] = None

        cols.add(c)
        diagonals[r+c] = True
        antidiagonals[r-c] = True

    for c in range(n):
        yield from dfs(0, c)


def find_boards(n):
    boards = set()
    for board in filter(bool, _find_boards(n)):
        boards.add(board)
    return boards


def leetcode_format(formatted_board):
    return ["".join(v or "." for v in row) for row in formatted_board.split("\n")]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return list(map(leetcode_format, find_boards(n)))

for i in range(10):  # range(5):
# for i in (8,):
    print(f"{i=}")
    t, n = benchmark(lambda: find_boards(i))
    print(t, len(n))
