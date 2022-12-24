from david import *

from itertools import product

INDICES = range(9)
CELLS = tuple(product(INDICES, repeat=2))
class Board:
    ##@staticmethod
    def from_leetcode(leetcode):
        b = Board(leetcode)
        for r, c in CELLS:
            try:
                v = int(leetcode[r][c]) - 1
            except:
                continue
            #assert isinstance(b, Board)
            b.set((r, c), v)
        return b

    ##@staticmethod
    def get_related(cell):
        return Board.get_group(cell) - set((cell,))

    ##@staticmethod
    def get_group(cell):
        group = set()
        r, c = cell
        for R in INDICES:
            group.add((R, c))
        for C in INDICES:
            group.add((r, C))

        box_r = r//3
        box_c = c//3
        for R in range(3*box_r, 3*box_r+3):
            for C in range(3*box_c, 3*box_c + 3):
                group.add((R, C))

        return group

    def __init__(self, leetcode):
        self.count = 0
        self.leetcode = leetcode
        self.board = {}
        # self.column_options = { c: set(INDICES) for c in CELLS }
        # self.row_options = { c: set(INDICES) for c in CELLS }
        # self.box_options =  { c: set(INDICES) for c in CELLS }
        self.unset_cells = set(CELLS)

    def update_leetcode(self):
        for cell in CELLS:
            r, c = cell
            v = self.board.get(cell)
            leetcode_value = str(v+1) if v is not None else '.'
            self.leetcode[r][c] = leetcode_value

    # def validate(self):
    #     for cell in CELLS:
    #         related = Board.get_related(cell)
    #         if cell not in self.board:
    #             assert cell in self.unset_cells
    #         else:
    #             for r in related:
    #                 assert self.board[cell] not in self.options[r]

    def get_options(self, cell):
        options = set(INDICES)
        for r in Board.get_group(cell) - self.unset_cells:
            options.discard(self.board[r])
            if not options:
                return options
        return options

    #@show
    def set(self, cell, value):
        #assert cell not in self.board
        #assert cell in self.unset_cells
        #assert value in self.get_options(cell)
        self.board[cell] = value
        self.unset_cells.remove(cell)

    #@show
    def unset(self, cell):
        #assert cell in self.board
        #assert cell not in self.unset_cells
        value = self.board[cell]
        #assert value not in self.get_options(cell)
        del self.board[cell]
        self.unset_cells.add(cell)

    #@show
    def solve(self):
        self.count += 1
        if self.count % 10000 == 0:
            # input(self.count)
            print(self.count, len(self.board))
        if not self.unset_cells:
            return True
        for cell in self.unset_cells:
            options = self.get_options(cell)
            if not options:
                return False
            for option in INDICES:
                if option not in self.get_options(cell):
                    #assert False
                    continue
                self.set(cell, option)
                if self.solve():
                    return True
                self.unset(cell)
        return False

    def show(self):
        clean = lambda v: '.' if v is None else str(v)
        self.update_leetcode()
        return '\n' + '\n'.join(''.join(row) for row in self.leetcode) + '\n'

    def __repr__(self):
        return f'B({len(self.board)})' #+ self.show()


def solve(board):
    b = Board.from_leetcode(board)
    b.solve()
    b.update_leetcode()
    return b


easy = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = easy
b = solve(board)
print(b.show())
