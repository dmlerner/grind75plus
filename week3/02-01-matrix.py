# two fifty four - three oh nine (15m)
# https://leetcode.com/problems/01-matrix/

from collections import deque
from itertools import product


def get_neighbors(mat, point):
    in_bounds = lambda size: lambda i: 0 <= i < size
    in_row_bounds = in_bounds(len(mat))
    in_col_bounds = in_bounds(len(mat[0]))
    for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = point[0] + dr, point[1] + dc
        if in_row_bounds(r) and in_col_bounds(c):
            yield r, c


def updateMatrix(mat):
    zero_indices = tuple(
        filter(
            lambda pos: mat[pos[0]][pos[1]] == 0,
            product(range(len(mat)), range(len(mat[0]))),
        )
    )
    frontier = deque(zero_indices)
    visited = set(zero_indices)
    while frontier:
        expansion_point = frontier.popleft()
        neighbors = filter(
            lambda neighbor: neighbor not in visited,
            get_neighbors(mat, expansion_point),
        )
        for neighbor in neighbors:
            mat[neighbor[0]][neighbor[1]] = (
                mat[expansion_point[0]][expansion_point[1]] + 1
            )
            visited.add(neighbor)
            frontier.append(neighbor)
    return mat


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
