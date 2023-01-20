'''
https://leetcode.com/problems/longest-repeating-character-replacement/
2:08
2:13 idea
2:19 CountHeap
2:28 might work
2:32 obobs fixed enough to run; 9/37 pass
2:39 fixed a logic error; 11/37
2:57 ugh I want a break
6:02 aight let's try again
6:06 remove one line, now 36/37 lol
6:20 works but slow
'''

from david import *
clean()

import heapq
from collections import Counter

class CountHeap:
    def __init__(self):
        self.elements = []
        self.counts = Counter()
        self.size = 0

    def add(self, element):
        self.counts[element] += 1
        self.heappush(element)
        # print(self.counts.values(), self.size)
        assert sum(self.counts.values()) == self.size

    def remove(self, element):
        self.counts[element] -= 1
        self.size -= 1
        assert sum(self.counts.values()) == self.size

    def heappush(self, element):
        self.size += 1
        keyed_element = (-self.counts[element], element)
        heapq.heappush(self.elements, keyed_element)
        return keyed_element

    def heappop(self):
        return heapq.heappop(self.elements)

    def peek(self):
        self.purge_stale()
        negative_count, element = self.elements[0]
        count = -negative_count
        return count, element

    def pop(self):
        count, element = self.peek()
        self.remove(element)
        return count, element

    @show
    def get_max_count(self):
        # breakpoint()
        max_count, element = self.pop()
        removed = [element]
        while len(self):
            count, element = self.peek()
            if count == max_count:
                self.pop()
                removed.append(element)
            else:
                break
        for element in removed:
            self.add(element)
        return max_count, removed

    @show
    def purge_stale(self):
        while self.elements:
            negative_count, element = self.elements[0]
            count = -negative_count
            if count != self.counts[element]:
                self.heappop()
            else:
                break

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr({ k: v for (k, v) in self.counts.items() if v})# + ':' + str(len(self)) + ':' + str(self.elements)

@show
def can_extend(count_heap, s, k, stop):
    # if len(count_heap) == 3:
        # breakpoint()
    if stop >= len(s):
        return False
    if len(count_heap) <= k:
        return True
    count, elements = count_heap.get_max_count()
    letters_to_convert = len(count_heap) - count
    if s[stop] not in elements:
        letters_to_convert += 1
    return letters_to_convert <= k

def get_longest_after_replacement(s, k):
    count_heap = CountHeap()
    start = 0
    stop = 0 # exclusive
    longest = 0

    while start < len(s):
        print('loop1')
        while can_extend(count_heap, s, k , stop):
            count_heap.add(s[stop])
            stop += 1
        longest = max(longest, stop - start)
        count_heap.remove(s[start])
        start += 1
        sl()

        print('loop2')
        while len(count_heap) and start < stop and start < len(s) and not can_extend(count_heap, s, k, stop):
            count_heap.remove(s[start])
            start += 1
        sl()

    return longest


s = 'aababba'
k = 1

s = 'abaa'
k = 0

s = 'abab'
k = 2
s ="AABABBA"
k = 1
s = "ABCCCCC"
k = 2
print(get_longest_after_replacement(s, k))
