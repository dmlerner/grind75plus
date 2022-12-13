# https://leetcode.com/problems/word-search-ii/
from itertools import chain

WORD_KEY = "$"


def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
    return trie

def find_words(grid, word_list):
    row_indices = range(len(grid))
    column_indices = range(len(grid[0]))

    def in_bounds(rc):
        r, c = rc
        return r in row_indices and c in column_indices

    def get(rc):
        r, c = rc
        return grid[r][c]

    def get_neighbors(rc):
        if rc is None:
            for row_index in row_indices:
                for column_index in column_indices:
                    yield row_index, column_index
            return

        r, c = rc
        offsets = (-1, 0), (1, 0), (0, -1), (0, 1)
        for (dr, dc) in offsets:
            neighbor = r + dr, c + dc
            if in_bounds(neighbor):
                yield neighbor

    def find_words(rc, next_letter_trie):
        # if WORD_KEY in next_letter_trie[get(rc)]:
        if WORD_KEY in next_letter_trie:
            yield next_letter_trie.pop(WORD_KEY)

        visited = set()

        for neighbor in get_neighbors(rc):
            if neighbor in visited:
                continue
            visited.add(neighbor)

            neighbor_letter = get(neighbor)
            if neighbor_letter not in next_letter_trie:
                continue

            yield from find_words(neighbor, next_letter_trie[neighbor_letter])
            visited.remove(neighbor)

    trie = build_trie(word_list)
    print(trie)
    yield from find_words(None, trie)
    # yield from chain(
    #     *(find_words((r, c), trie) for r in row_indices for c in column_indices)
    # )


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
assert set(find_words(board, words)) == {"oath", "eat"}

board = [["a"]]
words = ["a"]
# breakpoint()
assert set(find_words(board, words)) == {"a"}
