# https://leetcode.com/problems/longest-valid-parentheses/
from david import show, show_locals
# 5:32
# 5:46 mebbe
# 5:50 nah (149/231)
# 6:07 mebbe (79/231)

from functools import cache

def longest_valid_paren(s):
    length_by_start = {0:0} # length of valid sequences by start index
    last_start = 0
    length = 0
    n_open = 0
    max_length = 0

    for i, c in enumerate(s):
        length += 1
        if c == '(':
            n_open += 1
        else:
            if n_open == 0:
                # invalid, start a new measurement
                last_start = i+1
                length = 0
                n_open = 0
            else:
                if n_open == 1:
                    # valid, record the length
                    length_by_start[last_start] = length
                    max_length = max(max_length, length)
                n_open -= 1

    return max_length

def longest_valid_paren2(s):
    @show
    @cache
    def dp(i, u, c):
        if i == len(s):
            return 0
        if s[i] == '(':
            return max(dp(i+1, u+1, c), dp(i+1, 0, 0))
        start_over_at_next = dp(i+1, 0, 0)
        if u == 0:
            return start_over_at_next
        if u == 1:
            # BUG: what if soan doesn't use s[i+1]
            return start_over_at_next + 2*(c+1)
        return max(start_over_at_next, dp(i+1, u-1, c+1))
    return dp(0, 0, 0)

def valid(s, i, j):
    unmatched = 0
    for c in s[i:j+1]:
        if c == '(':
            unmatched += 1
        else:
            if unmatched == 0:
                return False
            unmatched -= 1
    return unmatched == 0

def longest_valid_paren3(s):
    length_by_start = {}
    max_length = 0
    last_valid_start = None
    last_valid_end = None
    stack = []
    for i, c in enumerate(s):
        # breakpoint()
        if c == '(':
            stack.append(i)
        else:
            # c == ')'
            if stack:
                start = stack.pop()
                if last_valid_end is None:
                    last_valid_end = i
                    last_valid_start = start
                    assert start == i - 1
                elif last_valid_end != i - 2:
                    last_valid_end = i
                    last_valid_start = start
                    # assert start == i - 1
                else:
                    last_valid_end = i

                length = i - last_valid_start + 1
                length_by_start[last_valid_start] = length
                max_length = max(max_length, length)
            else:
                last_valid_start = last_valid_end = None
                # length = 0
                # last_start = i + 1
        show_locals()
    # print(length_by_start)
    return max_length



def test(s, expected):
    actual = longest_valid_paren3(s)
    if actual != expected:
        print(s, expected, actual)
        assert False
    print()

# test(")()())", 4)
# test( "(()", 2)
# test( ")()", 2)
# test( "()(()", 2)
test("()(())", 6)
