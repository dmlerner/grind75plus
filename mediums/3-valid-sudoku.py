# https://leetcode.com/problems/valid-sudoku
# 1:05
# 1:14 done or probably, leetcode is down...


def is_valid_group(groups):
    desired = set(map(str, range(1, 10)))
    return all(map(desired.__eq__, map(set, groups)))


def box(board, i, j):
    for r in range(3 * i, 3 * (i + 1)):
        for c in range(3 * j, 3 * (j + 1)):
            yield board[r][c]


def is_valid_board(board):
    rows = board
    cols = zip(*board)
    boxes = (box(board, i, j) for i in range(3) for j in range(3))
    return all(map(is_valid_group, (rows, cols, boxes)))


easy = [
    "534678912",
    "672195348",
    "198342567",
    "859761423",
    "426853791",
    "713924856",
    "961537284",
    "287419635",
    "345286179",
]
print(is_valid_board(easy))
