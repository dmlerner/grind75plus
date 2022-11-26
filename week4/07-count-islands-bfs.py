# https://leetcode.com/problems/number-of-islands/
# four thirty seven - four fifty eight
from david import *
from collections import deque

LAND = "1"


def in_bounds(pt, dimensions):
    for i in (0, 1):
        if not (0 <= pt[i] < dimensions[i]):
            return False
    return True


def is_land(pt, grid):
    return grid[pt[0]][pt[1]] == LAND


# @show
def get_neighbors(grid, point, dimensions):
    r, c = point
    # in_bounds = lambda bound: lambda x: 0 <= x < bound
    return list(
        filter(
            lambda pt: is_land(pt, grid),
            # is_land,
            # lambda pt: grid[pt[0]][pt[1]] == LAND,
            filter(
                lambda pt: in_bounds(pt, dimensions),
                ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)),
            ),
        )
    )


def count_islands(grid):
    n_islands = 0
    frontier = deque([])
    seen = set()
    m, n = dimensions = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if len(seen) != m * n:
                if (i, j) not in seen:
                    seen.add((i, j))
                    if grid[i][j] == LAND:
                        frontier.append((i, j))
                        n_islands += 1
            while frontier:
                active = frontier.popleft()
                for neighbor in get_neighbors(grid, active, dimensions):
                    # print(neighbor)
                    if neighbor not in seen:
                        seen.add(neighbor)
                        frontier.append(neighbor)
    return n_islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(count_islands(grid))
