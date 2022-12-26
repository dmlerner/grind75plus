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
    diagonals = {i:True for i in range(0, 2*n-1)}
    antidiagonals = {i: True for i in range(-n+1, n)}

    # @showlistify
    def dfs(r):
        """
        attempt to place a queen at r, c
        """

        for C in tuple(cols):
            if diagonals[r+C] and antidiagonals[r-C]:
                assert board[r][C] is None
                board[r][C] = QUEEN
                cols.remove(C)
                if not cols:
                    yield format(board)

                diagonals[r+C] = False
                antidiagonals[r-C] = False
                yield from dfs(r+1)
                board[r][C] = None

                cols.add(C)
                diagonals[r+C] = True
                antidiagonals[r-C] = True

    yield from dfs(0)


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

# for i in range(10):  # range(5):
for i in (5,):
    t, n = benchmark(lambda: find_boards(i))
    print(t, n)
