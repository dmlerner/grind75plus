'''
https://leetcode.com/problems/decode-string/
8:05
8:11 _decode works for flat
8:24 I should probably parse R->L
and also stop leetcoding for the night...
'''
from david import sl

def _decode(s, i, j):
    decoded = []
    while i < len(s):
        open_idx = s.index('[', i)
        close_idx = s.index(']', open_idx+1)
        quantity = int(s[i:open_idx])
        pattern = s[open_idx+1: close_idx]
        decoded.append(quantity * pattern)
        i = close_idx + 1
    return ''.join(decoded)

DIGITS = set(map(str, range(10)))
OPEN = '['
CLOSE = ']'
def decode(s, i=0):
    i = 0
    if s[i] in DIGITS:
        digit = []
        while s[i] != OPEN:
            digit.append(s[i])
            i += 1
        digit = int(''.join(digit))
        assert s[i] == OPEN



    return digit * decode(s, i+1)






# s = "3[a]2[bc]"
# "3[a2[c]]"
# print(decode(s))
