# https://leetcode.com/problems/word-break/
# three thirty seven - three fourty eight

from functools import cache
from david import show


def can_break(word, words):
    words = set(words)
    max_length = max(map(len, words))

    @cache
    @show
    def can_break(i):
        if i == len(word):
            return True
        length = 1
        while True:
            if length > max_length:
                break
            stop_index_incl = i + length - 1
            if stop_index_incl >= len(word):
                break
            if word[i : stop_index_incl + 1] in words:
                if can_break(stop_index_incl + 1):
                    return True
            length += 1
        return False

    return can_break(0)


# three fourty nine - four oh three
def can_break_iterative(word, words):
    words = set(words)
    max_length = max(map(len, words))
    i = len(word) - 1  # inclusive
    dp = [False] * len(word) + [True]
    while i >= 0:
        for j in range(i + 1, len(word) + 1):
            if j - i > max_length:
                break
            if word[i:j] in words and dp[j]:
                dp[i] = True
                break
        i -= 1
    return dp[0]


word = "leetcode"
words = "leet", "code"
print(can_break_iterative(word, words))
