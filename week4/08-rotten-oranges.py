# https://leetcode.com/problems/rotting-oranges/submissions/
# 740-755pm
from collections import deque

EMPTY, FRESH, ROTTEN = 0, 1, 2


def get_oranges_by_type(grid):
    oranges_by_type = {FRESH: set(), ROTTEN: set(), EMPTY: set()}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            oranges_by_type[grid[i][j]].add((i, j))
    return oranges_by_type


def minutes_to_rot(grid):
    oranges_by_type = get_oranges_by_type(grid)
    n_fresh = len(oranges_by_type[FRESH])
    rows = len(grid)
    cols = len(grid[0])
    minutes = 0
    rotted = 0
    frontier = deque(list(oranges_by_type[ROTTEN]))
    next_level = []
    while frontier or next_level:

        if not frontier:
            frontier = deque(next_level)
            next_level = []
            minutes += 1

        i, j = frontier.popleft()
        for (ni, nj) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni][nj] == FRESH:
                    next_level.append((ni, nj))
                    rotted += 1
                    grid[ni][nj] = ROTTEN

    if rotted == len(oranges_by_type[FRESH]):
        return minutes
    return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(minutes_to_rot(grid))
