# https://leetcode.com/problems/n-queens/

from david import *
from typing import *
import copy

QUEEN = 'Q'

def format(board):
    def row_format(row):
        return ''.join(i if i is not None else '.' for i in row)
    return '\n'.join(map(row_format, board))


def _find_boards(n):
    board = [[None]*n for i in range(n)]
    def dfs(r, c, remaining):
        '''
        attempt to place a queen at r, c
        '''
        assert remaining >= 1
        assert sum(row.count(QUEEN) for row in board) <= n

        if board[r][c] is not None:
            return

        board[r][c] = QUEEN
        remaining -= 1
        if is_valid(board):
            if remaining == 0:
                yield format(board)
            else:
                for R in range(n):
                    for C in range(n):
                        # optimization. unclear if it skips solutions.
                        if (R, C) > (r, c):
                            yield from filter(bool, dfs(R, C, remaining))
                    # if (solution := ):
                    #     yield solution

        board[r][c] = None

    for r in range(n):
        for c in range(n):
            yield from dfs(r, c, n)

def find_boards(n):
    boards = set()
    for board in filter(bool, _find_boards(n)):
        boards.add(board)
    return boards

def rising_diagonal(n, i):
    ''' in an nxn board,
    yield the coordinates of the ith diagonal.
    number main diagonal out.
    positive i is below the diagonal.
    '''
    assert -n < i < n
    length = n - abs(i)
    if i < 0:
        start = n-1+i, 0
    else:
        start = n-1, i
    for l in range(length):
        yield start[0] - l, start[1] + l

def falling_diagonal(n, i):
    assert -n < i < n
    length = n - abs(i)
    if i > 0:
        start = i, 0
    else:
        start = 0, -i
    for l in range(length):
        yield start[0] + l, start[1] + l


def is_valid(board):
    n = len(board)
    def valid(rcs):
        rcs = list(rcs)
        return len(tuple(filter(lambda rc: board[rc[0]][rc[1]] == QUEEN, rcs))) <= 1
    for r in range(n):
        row = ((r, c) for c in range(n))
        if not valid(row):
            return False
    for c in range(n):
        col = ((r, c) for r in range(n))
        if not valid(col):
            return False
    for i in range(-n+1, n):
        if not valid(rising_diagonal(n, i)):
            return False
    for i in range(-n+1, n):
        if not valid(falling_diagonal(n, i)):
            return False
    return True

def from_leetcode(board):
    #[".Q..","...Q","Q...","..Q."]
    return [[c if c == QUEEN else None for c in row] for row in board]

def leetcode_format(formatted_board):
    return [''.join(v or '.' for v in row) for row in formatted_board.split('\n')]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return list(map(leetcode_format, find_boards(n)))
# assert is_valid(from_leetcode([".Q..","...Q","Q...","..Q."]))
# assert not is_valid(from_leetcode([".Q..","...Q","Q...","..Q."]))
# 1/0

for i in (4,):#range(5):
    boards = find_boards(i)
    print(boards)
    assert boards
    for board in boards:
        assert is_valid(from_leetcode(leetcode_format(board)))


assert list(rising_diagonal(3, 0)) == [(2,0), (1,1), (0,2)]
assert list(falling_diagonal(3, 0)) == [(0, 0), (1, 1), (2,2)]
assert list(falling_diagonal(4, -1))  == [(0,1),(1,2),(2,3)]


