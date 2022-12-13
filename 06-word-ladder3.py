from collections import deque

def add_wildcards(word):
    for i in range(len(word)):
        yield word[:i], word[i], word[i+1:]

def get_neighbors(word):
    if '*' in word:
        pass
    else:
        yield from add_wildcards(word)

def bfs(start, stop):
    frontier = deque([start])
    visited = set()
    while frontier:
        active = frontier.popleft()
        for neighbor in get_neighbors(active):
            if neighbor not in visited:
                yield neighbor
                if neighbor == stop:
                    return
                visited.add(neighbor)
                frontier.append(neighbor)

def ladder_length(start, stop, words):
    words = set(words)
    for word in bfs(start, stop):
