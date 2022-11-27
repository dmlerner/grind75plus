# https://leetcode.com/problems/word-search/
# two thirty five - two fourty for very close solution
# exceptions were causing DLE
# then fails on 1x1 grid
# then fails on a nontivial example (non-DLE) two fifty five
# fix careless +1 at two fifty seven
# fix other careless -1 at three oh three
# and back to DLE...
# three oh nine - add counter early check
# now above median speed
# well that's silly

def exists(grid, word):
    def in_bounds(ij):
        i, j = ij
        return 0 <= i < in_bounds.ROWS and 0 <= j < in_bounds.COLS

    in_bounds.ROWS = len(grid)
    in_bounds.COLS = len(grid[0])

    def get_neighbors(i, j):
        return list(filter(in_bounds, ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))))

    def dfs(i, j, c):
        if c >= len(word):
            return False
        if c == 0:
            assert not any(x is None for row in grid for x in row)
        # can I find word[c:] starting at grid[i][j]?
        if grid[i][j] == word[c]:
            c += 1
            if c == len(word):
                return True

            grid[i][j] = None
            if any(dfs(ni, nj, c) for (ni, nj) in get_neighbors(i, j)):
                return True
            grid[i][j] = word[c-1]

        return False

    word_letter_counts = Counter(word)
    grid_letter_counts = count_letters(grid)
    for letter in word_letter_counts:
        if grid_letter_counts[letter] < word_letter_counts[letter]:
            return False

    return any(dfs(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])))

from collections import Counter
def count_letters(grid):
    c = Counter()
    for row in grid:
        for letter in row:
            c[letter] += 1
    return c



grid = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]
word = "AAAAAAAAAAAAAAB"

# grid = [["a"]]
# word = "a"

# grid = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E"]
# ]
# word = "ABCCED"
# grid = [["C","A","A"],
#         ["A","A","A"],
#         ["B","C","D"]]
# word = "AAB"
print(exists(grid, word))
