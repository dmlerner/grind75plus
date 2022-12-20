# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 8:05
# 8:13 naive dfs implemented
# 8:18 I should use visited set, not overwrite with None
# otherwise get_neighbors can't do the self < neighbor check
# also because ew
# 8:22 135/138 cases pass (3 DLE)
# 8:38 start coding faster idea
# 9:03 returns 3, should be 4
# day job oh clock

from david import *
from collections import namedtuple, deque
from functools import cache


def longest_path(matrix):
    in_current_path = set()

    def get_neighbors(rc, matrix):
        r, c = rc

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) in in_current_path:
                continue
            if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0])):
                continue
            if matrix[nr][nc] > matrix[r][c]:
                yield nr, nc

    def dfs(rc, matrix):
        longest = 1

        r, c = rc
        in_current_path.add(rc)

        for nr, nc in get_neighbors(rc, matrix):
            longest = max(longest, 1 + dfs((nr, nc), matrix))

        in_current_path.remove(rc)

        return longest

    return max(
        dfs((r, c), matrix) for r in range(len(matrix)) for c in range(len(matrix[0]))
    )


# problem: there are multiple such paths!
sl=show_locals

from collections import namedtuple, deque
from functools import cache
Path = namedtuple("Path", "start end length")

def longest_path2(matrix):
    def get_four_connected(rc):
        r, c = rc
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0])):
                continue
            yield nr, nc

    def get(rc):
        r, c = rc
        return matrix[r][c]

    @cache
    # @show
    # @recursion_limit
    def longest_path_from(start):
        path = Path(start, start, 1)
        best_path = path

        for rc2 in get_four_connected(path.end):
            if not get(path.end) < get(rc2):
                continue
            tail = longest_path_from(rc2)
            combined_length = tail.length + path.length
            longer = combined_length > best_path.length
            same_length = combined_length == best_path.length
            # This is irrelevant. 
            # If a tie being broken by this were to matter,
            # that path would have to end up longer
            # but it didn't, by definition!
            lower_end_value = get(tail.end) < get(best_path.end)
            # sl()
            if longer or (same_length and lower_end_value):
                best_path = Path(path.start, tail.end, combined_length)
        return best_path

    @cache
    def i_cheated(start):
        m = 1
        for rc2 in get_four_connected(start):
            if get(rc2) > get(start):
                m = max(i_cheated(rc2) + 1, m)
        return m


    R, C = len(matrix), len(matrix[0])
    row_indices = range(R)
    col_indices = range(C)
    longest = 1
    for row in row_indices:
        for col in col_indices:
            longest = max(longest, i_cheated((row, col)))
            # longest = max(longest, longest_path_from((row, col)).length)

    return longest


matrix = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
    [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
    [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# matrix = [[9, 9, 4],
#           [6, 6, 8],
#           [2, 1, 1]]

matrix = [[2, 3],
          [1, 2]]

# matrix = [[0]]

matrix = [[3,4,5],
          [3,2,6],
          [2,2,1]]

matrix = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12, 13],
    [14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 31, 32, 33, 34],
    [35, 36, 37, 38, 39, 40, 41],
    [42, 43, 44, 45, 46, 47, 48],
]


lp = longest_path2(matrix)
print()
print(lp)
