# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# three thirteen - three thiryt one for potentially correct
# three thirty seven - pass 26/61
# four o clock:pass 33/61, take a walk (refactored to count things in p even when they're extra)
# four oh one: I was lying, fix minor bug, passes.
# TODO: try this beast again.

from collections import Counter


class LetterCounter:
    def __init__(self, p):
        self.p_counts = Counter(p)
        self.counts = Counter()
        self.need = set(self.p_counts.keys())
        self.extra = 0

    def add(self, x):
        # print('add', self.need, x, self.n_need, self.extra)
        if x not in self.p_counts:
            self.extra += 1
            return

        self.counts[x] += 1
        if self.counts[x] == self.p_counts[x]:
            self.need.remove(x)
        elif self.counts[x] > self.p_counts[x]:
            self.extra += 1

    def remove(self, x):
        if x not in self.counts:
            self.extra -= 1
            return

        self.counts[x] -= 1
        if self.counts[x] < self.p_counts[x]:
            self.need.add(x)
        else:
            self.extra -= 1


def find(s, p):
    # Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    # You may return the answer in any order.
    lc = LetterCounter(p)
    i = j = 0
    indices = []
    # invariant: s_counts contains the counts of s[i:j]
    while i <= len(s):
        # lc.add(s[i])
        if not lc.need:
            if lc.extra == 0:
                indices.append(i)
            lc.remove(s[i])
            i += 1
        else:
            if j == len(s):
                break
            lc.add(s[j])
            j += 1

    return indices


s = "abab"
p = "ab"
print(find(s, p))
