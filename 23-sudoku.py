# https://leetcode.com/problems/sudoku-solver/
# 1:50
# 2:05 gratuitious board class done
# 2:50 naive dfs is clearly not going to cut it. gets 65/81 cells
# 3:06 works pretty fast! now to submit...

from david import *

class Board:
    def __init__(self, board):
        self._board = board
        self.count = 0
        # self.options = [[set(range(9)) for c in range(9)] for r in range(9)]
        # self.rows = [set() for i in range(9)]
        self.row_options = [set(range(9)) for r in range(9)]
        # self.cols = [set() for i in range(9)]
        self.col_options =  [set(range(9)) for c in range(9)]
        # self.boxes = [[set() for i in range(3)] for j in range(3)]
        self.box_options = [[set(range(9)) for i in range(3)] for j in range(3)]
        self.size = 0
        self.unset = set((r, c) for r in range(9) for c in range(9))

        self.board = [[None]*9 for c in range(9)]
        for r in range(9):
            for c in range(9):
                try:
                    v = int(board[r][c]) - 1
                except:
                    continue
                self.set(r, c, v)

    def get_sub_options(self, r, c):
        return [self.row_options[r], self.col_options[c], self.box_options[r//3][c//3]]

    # @show
    def get_options(self, r, c):
        if self.board[r][c] is not None:
            return set()

        # TODO: cache?
        sub_options = self.get_sub_options(r, c)
        sub_options.sort(key=len)
        return sub_options[0].intersection(sub_options[1]).intersection(sub_options[2])


    # @show
    def set(self, r, c, v):
        assert self.board[r][c] is None
        assert v in self.get_options(r, c)
        sub_options = self.get_sub_options(r, c)
        found = 0
        for o in sub_options:
            if v in o:
                found += 1
                o.remove(v)
        assert found
        self.board[r][c] = v
        self.size += 1
        self.unset.remove((r, c))

    def remove(self, r, c):
        assert self.board[r][c] is not None
        v = self.board[r][c]
        for sub_option in self.get_sub_options(r, c):
            assert v not in sub_option
            sub_option.add(v)
        self.board[r][c] = None
        self.size -= 1
        self.unset.add((r, c))

    def get_related(self, r, c):
        for C in range(9):
            if C != c:
                yield r, C
        for R in range(9):
            if R != r:
                yield R, c
        yield from filter(lambda rc: rc != (r, c), self.get_box(r, c))

    def get_box(self, r, c):
        box_r = r//3
        box_c = c//3
        for r in range(box_r, box_r+3):
            for c in range(box_c, box_c + 3):
                yield r, c

    # @show
    def set_determined(self):
        determined = set()
        for r in range(9):
            for c in range(9):
                options = self.get_options(r, c)
                if len(options) == 1:
                    option = options.pop()
                    determined.add((r, c))
                    self.set(r, c, option)
        return determined


    # @show
    def solve(self):
        if self.size == 81:
            raise SolvedException()
        self.count += 1
        for (r, c) in self.unset:
            # error: self.options changes in sub calls?
            options = self.get_options(r, c)
            for v in options:
                self.set(r, c, v)
                determined = self.set_determined()
                self.solve()
                self.remove(r, c)
                for (dr, dc) in determined:
                    self.remove(dr, dc)

        # if self.count % 10000 == 0:
        #     print(self.count, self.size)


    def show(self):
        clean = lambda v: '.' if v is None else str(v)
        return str(self.size) + '\n' + '\n'.join(''.join(map(clean, row)) for row in self.board) + '\n'

    def __repr__(self):
        return f'B({self.size})'

    def format(self):
        for r in range(9):
            for c in range(9):
                v = self.board[r][c]
                if v is None:
                    f = '.'
                else:
                    v = str(v + 1)
                self._board[r][c] = v




def solve(board):
    b = Board(board)
    for r in range(9):
        for c in range(9):
            if b.board[r][c] is None:
                assert (r, c) in b.unset
            else:
                assert (r, c) not in b.unset
                assert not b.get_options(r, c)
    try:
        b.solve()
    except SolvedException:
        pass
    b.format()

class SolvedException(Exception):
    pass

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        solve(board)


b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
b = solve(b)

