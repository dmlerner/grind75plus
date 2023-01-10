"""
new idea: build counts first
muchhhh better.
"""

import heapq
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class WordCount:
    word: str
    count: int

    def __lt__(self, other):
        if self.count < other.count:
            return True
        if self.count > other.count:
            return False
        assert self.word != other.word
        return self.word > other.word


def top_k(words, k):
    count_by_word = Counter(words)
    heap = []
    for word, count in count_by_word.items():
        heapq.heappush(heap, WordCount(word, count))
        if len(heap) > k:
            heapq.heappop(heap)
    while heap:
        yield heapq.heappop(heap).word


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(list(reversed(list(top_k(words, k)))))
