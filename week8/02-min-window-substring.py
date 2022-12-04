# https://leetcode.com/problems/minimum-window-substring/
# twelve twenty - twelve fifty two
from david import *

from collections import Counter


def min_window_substring(s, t):
    i = j = 0
    need_counts = Counter(t)
    need = set(t)
    mws = None
    while i < len(s) and j < len(s):
        while need and j < len(s):
            if s[j] in need_counts:
                need_counts[s[j]] -= 1
                if need_counts[s[j]] == 0:
                    need.remove(s[j])
            j += 1
        while not need:
            candidate_mws = s[max(0, i):j]
            if mws is None or len(candidate_mws) < len(mws):
                mws = candidate_mws

            if s[i] in need_counts:
                need_counts[s[i]] += 1
                if need_counts[s[i]] == 1:
                    need.add(s[i])
            i += 1
    return mws



s="ADOBECODEBANC"
t="ABC"
# breakpoint()

s="a"
t="aa"

print(min_window_substring(s, t))

