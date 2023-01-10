"""
https://leetcode.com/problems/top-k-frequent-words/
12:27
12:51 maybe
12:53 no, ordering by count then letters, not just letters
12:57 almost, but bug: remove ties from heap
[a few minute break]
1:08 done, but slow
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


class Heap:
    def __init__(self):
        self.heap = []
        self.deleted = set()

    def clear_deleted(self):
        while self.peek() in self.deleted:
            self._pop()

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        self.clear_deleted()
        return self._pop()

    def _pop(self):
        popped = heapq.heappop(self.heap)
        if popped in self.deleted:
            self.deleted.remove(popped)
        else:
            return popped

    def peek(self):
        return self.heap[0]

    def delete(self, x):
        self.deleted.add(x)

    def __len__(self):
        return len(self.heap) - len(self.deleted)

    def __iter__(self):
        while self.heap:
            yield self.pop()

    def __reversed__(self):
        return reversed(list(self))


def order(counts_and_words):
    last_count = None
    group = []
    for wc in counts_and_words:
        word, count = wc.word, wc.count
        if count == last_count:
            group.append(word)
        else:
            yield from sorted(group)
            group = [word]
            last_count = count
    yield from sorted(group)


def top_k(words, k):
    counts = Counter()
    heap = Heap()
    heap_words = set()

    for word in words:
        count = counts[word]
        if word in heap_words:
            heap.delete(WordCount(word, count))
        counts[word] += 1
        heap.push(WordCount(word, count + 1))
        heap_words.add(word)
        if len(heap) == k + 1:
            popped = heap.pop()
            heap_words.remove(popped.word)
        assert len(heap) <= k

    return list(order(reversed(heap)))


words = ["i", "love", "leetcode", "i", "love", "coding"]
print(top_k(words, 1))
