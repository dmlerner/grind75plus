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
Path = namedtuple("Path", "start end length")


def longest_path2(matrix):
    def get_four_connected(rc):
        r, c = rc
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0])):
                continue
            yield nr, nc

    # @show
    def combine(p1, p2):
        if not p1 or not p2:
            assert False
            return False
        assert isinstance(p1, Path)
        assert isinstance(p2, Path)

        r1, c1 = p1.end
        r2, c2 = p2.start
        if not matrix[r1][c1] < matrix[r2][c2]:
            return

        return Path(p1.start, p2.end, p1.length + p2.length)

    def get_extensions(path):
        for adjacent in get_four_connected(path.end):
            for end, tail in paths_by_start[adjacent].items():
                if combined := combine(path, tail):
                    yield combined

    # @show
    def dfs(path):
        # print()
        # print('start')
        # breakpoint()
        nonlocal longest, count
        # print(count, sum(map(len, paths_by_start.values())))
        assert count == sum(map(len, paths_by_start.values()))
        # print(count, paths_by_start)
        # print(count)
        # if count == 5:
        #     breakpoint()
        if paths_by_start[path.start][path.end].length > path.length:
            return
        del paths_by_start[path.start][path.end]
        count -= 1
        for extension in get_extensions(path):
            longest = max(longest, extension.length)
            assert extension not in paths_by_start[path.start]
            p = paths_by_start[path.start].get(extension.end)
            if not p or p.length < extension.length:
                paths_by_start[path.start][extension.end] = extension
            if not p:
                count += 1
            dfs(extension)
        else:
            assert path.end not in paths_by_start[path.start]
            paths_by_start[path.start][path.end] = path
            count += 1

        # print('end')
        # print()

    R, C = len(matrix), len(matrix[0])
    row_indices = range(R)
    col_indices = range(C)
    longest = 1
    # { start: { end: longest known Path }}
    paths_by_start = {
        (r, c): {(r, c): Path((r, c), (r, c), 1)}
        for r in row_indices
        for c in col_indices
    }
    count = R * C
    start_paths = {
        Path((r, c), (r, c), 1) for r in row_indices for c in col_indices
    }  # p.values for paths in paths_by_start.values() for p in paths}
    for p in start_paths:
        dfs(p)

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

matrix = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12, 13],
    [14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 31, 32, 33, 34],
    [35, 36, 37, 38, 39, 40, 41],
    [42, 43, 44, 45, 46, 47, 48],
]

# matrix = [[9, 9, 4],
#           [6, 6, 8],
#           [2, 1, 1]]

# matrix = [[2, 3], [1, 2]]

# matrix = [[0]]

# matrix = [[3,4,5],[3,2,6],[2,2,1]]
lp = longest_path2(matrix)
print()
print(lp)
