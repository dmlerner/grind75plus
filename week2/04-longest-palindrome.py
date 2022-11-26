# https://leetcode.com/problems/longest-palindrome/
# fuck manacher
# 15:52
# 16:08 I realize that it means I can reorder the letters
# 16:11 done
from david import show

@show
def longest_odd_palindrome_at(s, i):
    return 2*_longest_palindrome_at(s, i, i-1, i+1) + 1

@show
def longest_even_palindrome_at(s, i):
    # with center between i and i + 1
    return 2*_longest_palindrome_at(s, i, i, i+1)

@show
def _longest_palindrome_at(s, i, left, right):
    matches = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        matches += 1
        left -= 1
        right += 1
    return matches

@show
def longest_palindrome_at(s, i):
    return max(longest_even_palindrome_at(s, i), longest_odd_palindrome_at(s, i))


@show
def longest_pal(s):
    return max(map(lambda i: longest_palindrome_at(s, i), range(len(s))))

# print(longest_pal("abccccdd"))

# can use all even-count letters
# and zero or one odd-count
from collections import Counter
def longest_pal(s):
    counts = Counter(s)
    length = 0
    odd_count_found = False
    for letter, count in counts.items():
        length += count - count%2
        odd_count_found |= count % 2
    return length + odd_count_found


