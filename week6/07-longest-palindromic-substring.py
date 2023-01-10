# https://leetcode.com/problems/longest-palindromic-substring/
# ten twenty - ten thirty six
# stealing some code from the easy version of this problem (week2/04-longest-palindrome.py)
# I still refuse to implment manacher or fancy lca shit
from david import show


def longest_odd_palindrome_at(s, i):
    radius = _longest_palindrome_at(s, i - 1, i + 1)
    return 2 * radius + 1, s[i - radius : i + radius + 1]


def longest_even_palindrome_at(s, i):
    # with center between i and i + 1
    radius = _longest_palindrome_at(s, i, i + 1)
    return radius * 2, s[i - radius + 1 : i + radius + 1]


def _longest_palindrome_at(s, left, right):
    matches = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        matches += 1
        left -= 1
        right += 1
    return matches


def longest_palindrome_at(s, i):
    return max(longest_even_palindrome_at(s, i), longest_odd_palindrome_at(s, i))


def longest_pal(s):
    return max(map(lambda i: longest_palindrome_at(s, i), range(len(s))))[1]


lp = longest_pal("babad")
print(lp)
