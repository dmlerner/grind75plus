# https://leetcode.com/problems/number-of-islands/
# four thirty seven - four fifty eight
from david import *
from functools import wraps

LAND = "1"
WATER = "0"
VISITED = None


def bound_safe(default=None):
    def decorator(f):
        @wraps(f)
        def _f(*args, **kwargs):
            try:
                f(*args, **kwargs)
            except IndexError:
                return default

        return _f

    return decorator


@bound_safe()
def dfs_fill(grid, i, j):
    if i < 0 or j < 0:
        raise IndexError
    if grid[i][j] != LAND:
        return
    grid[i][j] = VISITED

    for (r, c) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        dfs_fill(grid, r, c)
        # if grid[r][c] == LAND:
        #     dfs_fill(grid, r, c)


def count_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == LAND:
                print("start", i, j, grid)
                count += 1
                dfs_fill(grid, i, j)
    return count


# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
# ]

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"],
# ]

grid = [["1", "0", "1", "1", "0", "1", "1"]]
print(count_islands(grid))
