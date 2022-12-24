# https://leetcode.com/problems/sudoku-solver/
# 1:50
# 2:05 gratuitious board class done
# 2:50 naive dfs is clearly not going to cut it. gets 65/81 cells
# 3:06 works pretty fast! now to submit...
# 3:37 bugging caching of options but might be faster...

from david import *

from collections import deque

class Board:
    def __init__(self, board):
        self._board = board
        self.count = 0
        self.options = [[set(range(9)) for c in range(9)] for r in range(9)]
        self.size = 0
        self.unset = set((r, c) for r in range(9) for c in range(9))

        self.board = [[None]*9 for c in range(9)]
        for r in range(9):
            for c in range(9):
                try:
                    v = int(board[r][c]) - 1
                except:
                    continue
                # if (r, c) == (1, 5):
                    # breakpoint()
                self.set(r, c, v)
                # print(self.show())


    @show
    def get_options(self, r, c):
        if self.board[r][c] is not None:
            return set()
        return self.options[r][c]

    @show
    def set(self, r, c, v):
        assert self.board[r][c] is None
        assert v in self.options[r][c]
        self.board[r][c] = v
        for (R, C) in self.get_related(r, c):
            # need to remove the option even if R,C is occupied
            # do, don't call get_options(R, C)
            options = self.options[R][C]
            if v in options:
                options.remove(v)
        self.size += 1
        self.unset.remove((r, c))

    @show
    def remove(self, r, c):
        assert self.board[r][c] is not None
        v = self.board[r][c]
        self.board[r][c] = None
        for (R, C) in self.get_related(r, c):
            self.options[R][C].add(v)
        self.size -= 1
        self.unset.add((r, c))

    @showlistify
    def get_related(self, r, c):
        for C in range(9):
            yield r, C
        for R in range(9):
            yield R, c
        yield from self.get_box(r, c)

    def get_box(self, r, c):
        box_r = r//3
        box_c = c//3
        for R in range(3*box_r, 3*box_r+3):
            for C in range(3*box_c, 3*box_c + 3):
                yield R, C

    @show
    def set_determined(self, r, c):
        determined = set([(r, c)])
        # this could be a stack just as easily...
        frontier = [(r, c)]
        while frontier:
            active = frontier.pop()
            for related in self.get_related(*active):
                if related in determined:
                    continue
                R, C = related
                # use get_options so if related is occupied, we don't use it
                options = self.get_options(R, C)
                if len(options) == 1:
                    # don't pop - throws off invariants
                    option = tuple(options)[0]
                    determined.add(related)
                    frontier.append(related)
                    self.set(*related, option)
        return determined


    @show
    def solve(self):
        if self.size == 81:
            raise SolvedException()
        # if self.size == 80:
        #     breakpoint()
        self.count += 1
        for (r, c) in self.unset:
            assert self.board[r][c] is None
            options = self.get_options(r, c)
            # if (r, c) == (8, 0):
            #     sl()
            #     breakpoint()
            # if options == {2, 3, 5, 7} and self.size == 47 and (r, c) == (8, 0):
            #     breakpoint()
            for v in options:
                self.set(r, c, v)
                # TODO: consider passing r, c
                determined = self.set_determined(r, c)
                self.solve()
                # Not needed: this will be in determined
                assert (r, c) in determined
                for (dr, dc) in determined:
                    if (dr, dc) == (r, c):
                        continue
                    self.remove(dr, dc)
                self.remove(r, c)

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
    # print('.'*100)
    try:
        b.solve()
    except SolvedException:
        pass
    b.format()
    return b

class SolvedException(Exception):
    pass

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        solve(board)

# def get_box(r, c):
#     box_r = r//3
#     box_c = c//3
#     for r in range(3*box_r, 3*box_r+3):
#         for c in range(3*box_c, 3*box_c + 3):
#             yield r, c
# print(list(get_box(0, 0)))
# print(list(get_box(7, 8)))
# 1/0
b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
b = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
b = solve(b)
print(b.show())

