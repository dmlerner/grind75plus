# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# seven fourteen - seven twenty four

from collections import Counter


def longest(s):
    c = Counter()
    i = j = 0
    max_length = 0
    while j < len(s):
        # invariant: s[i:j] contains distinct characters
        if c[s[j]] == 0:
            c[s[j]] += 1
            j += 1
            max_length = max(max_length, j - i)
        else:
            while c[s[j]] != 0:
                c[s[i]] -= 1
                i += 1
    return max_length
