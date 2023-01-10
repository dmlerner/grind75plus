from collections import deque


def in_bounds(image, r, c):
    return 0 <= r < len(image) and 0 <= c < len(image[0])


OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def get_neighbors(image, r, c, color):
    for (dr, dc) in OFFSETS:
        nr, nc = neighbor = r + dr, c + dc
        if not in_bounds(image, *neighbor):
            continue
        neighbor_color = image[nr][nc]
        if image[nr][nc] != color:
            continue
        yield neighbor


def bfs(start, get_neighbors):
    frontier = deque([start])
    enqueued = {
        start
    }  # TODO: could this start empty if I add after appending to queue?
    while frontier:
        active = frontier.popleft()
        yield active
        neighbors = get_neighbors(active)
        unenqueued_neighbors = filter(lambda n: n not in visited, neighbors)
        for neighbor in unenqueued_neighbors:
            frontier.append(neighbor)
            enqueued.add(neighbor)


# https://leetcode.com/problems/flood-fill/
def fill(image, sr, sc, target_color):
    start = sr, sc
    frontier = deque([start])
    enqueued = set(start)
    filter_color = image[sr][sc]
    image[sr][sc] = target_color
    while frontier:
        active = frontier.popleft()
        neighbors = get_neighbors(image, *active, filter_color)
        unenqueued_neighbors = filter(lambda n: n not in visited, neighbors)
        for r, c in unenqueued_neighbors:
            image[r][c] = target_color
            frontier.append((r, c))
            enqueued.add((r, c))
    return image


def bfs2(start, get_neighbors):
    frontier = deque([start])
    enqueued = set(start)

    def update(n):
        frontier.append(n)
        enqueued.add(n)

    while frontier:
        active = frontier.popleft()
        yield active
        neighbors = get_neighbors(active)
        unenqueued_neighbors = filter(lambda n: n not in visited, neighbors)
        any(map(update, unenqueued_neighbors))


def fill2(image, sr, sc, target_color):
    filter_color = image[sr][sc]

    def _get_neighbors(rc):
        return get_neighbors(image, *rc, filter_color)

    for (r, c) in bfs2((sr, sc), _get_neighbors):
        image[r][c] = target_color
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(f"{image=}")
new_image = fill2(image, 1, 1, 2)
print(f"{new_image=}")
expected_new_image = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(f"{expected_new_image=}")
assert new_image == expected_new_image
print("tests pass")
