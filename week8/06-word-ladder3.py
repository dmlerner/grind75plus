from collections import deque, defaultdict


def add_wildcards(word):
    for i in range(len(word)):
        yield "".join((word[:i], "*", word[i + 1 :]))


def get_neighbors(word):
    if "*" in word:
        pass
    else:
        yield from add_wildcards(word)


def build_edges(words):
    words = set(words)
    edges = defaultdict(set)
    for word in words:
        for wildcarded in add_wildcards(word):
            edges[word].add(wildcarded)
            edges[wildcarded].add(word)
    return edges


def bfs(start, stop, edges):
    frontier = deque([start])
    visited = set()
    dist = {start: 1}
    while frontier:
        active = frontier.popleft()
        for neighbor in edges[active]:
            if neighbor not in visited:
                dist[neighbor] = dist[active] + 1
                yield neighbor, dist[neighbor]
                if neighbor == stop:
                    return
                visited.add(neighbor)
                frontier.append(neighbor)


def ladder_length(start, stop, words):
    edges = build_edges(words + [start])
    for word, dist in bfs(start, stop, edges):
        if word == stop:
            return dist // 2 + 1
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladder_length(beginWord, endWord, wordList))
