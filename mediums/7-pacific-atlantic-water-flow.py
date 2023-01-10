"""
6:48
https://leetcode.com/problems/pacific-atlantic-water-flow/
7:01
first submission
...although I ran a few times locally
"""

from collections import deque


def in_bounds(heights, r, c):
    return 0 <= r < len(heights) and 0 <= c < len(heights[0])


def get_neighbors(heights, r, c):
    offsets = (-1, 0), (1, 0), (0, -1), (0, 1)
    height = heights[r][c] if in_bounds(heights, r, c) else float("-inf")
    for dr, dc in offsets:
        nr, nc = r + dr, c + dc
        if in_bounds(heights, nr, nc):
            if heights[nr][nc] >= height:
                yield nr, nc


def get_sources(heights, sinks):
    """sinks is either pacific or atlantic"""
    sources = []
    visited = set()
    frontier = deque(sinks)

    while frontier:
        active = frontier.popleft()

        for neighbor in get_neighbors(heights, *active):
            if neighbor in visited:
                continue

            visited.add(neighbor)
            frontier.append(neighbor)
            sources.append(neighbor)

    return sources


def get_pacific(heights):
    R, C = len(heights), len(heights[0])
    return [(-1, c) for c in range(C)] + [(r, -1) for r in range(R)]


def get_atlantic(heights):
    R, C = len(heights), len(heights[0])
    return [(R, c) for c in range(C)] + [(r, C) for r in range(R)]


def pacific_atlantic(heights):
    pacific = get_pacific(heights)
    atlantic = get_atlantic(heights)
    return list(
        set(get_sources(heights, pacific)) & set(get_sources(heights, atlantic))
    )


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacific_atlantic(heights))
