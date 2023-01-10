"""
https://leetcode.com/problems/shortest-path-to-get-food/
11:36
11:49 should be working but isn't uhhhh
11:52 done - had `if active in visited` oops
"""

from collections import deque

START = "*"
OBSTACLE = "X"
FREE = "O"
FOOD = "#"


def in_bounds(rc, grid):
    return 0 <= rc[0] < len(grid) and 0 <= rc[1] < len(grid[0])


def get_connected(rc, grid):
    r, c = rc
    offsets = (-1, 0), (1, 0), (0, -1), (0, 1)
    for dr, dc in offsets:
        neighbor = r + dr, c + dc
        if in_bounds(neighbor, grid):
            yield neighbor


def get(rc, grid):
    r, c = rc
    return grid[r][c]


def find(symbol, grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if get((r, c), grid) == symbol:
                return r, c


def shortest_path_to_food(grid):
    start = find(START, grid)
    assert start

    visited = set([start])
    frontier = deque([start])
    length_by_rc = {start: 0}
    while frontier:
        active = frontier.popleft()
        for neighbor in get_connected(active, grid):
            if neighbor in visited:
                continue
            length_by_rc[neighbor] = length_by_rc[active] + 1
            visited.add(neighbor)

            neighbor_value = get(neighbor, grid)
            if neighbor_value == FOOD:
                return length_by_rc[neighbor]
            if neighbor_value == OBSTACLE:
                continue
            if neighbor_value == FREE:
                frontier.append(neighbor)

    return -1


grid = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "O", "O", "X"],
    ["X", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X"],
]
print(shortest_path_to_food(grid))
