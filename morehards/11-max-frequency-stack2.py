# twelve fifty eight
# let's try a "lazy delete" approach
import heapq
from collections import Counter, namedtuple

Datum = namedtuple("Datum", "value count t")
Datum.__lt__ = lambda self, other: self.count > other.count or self.count == other.count and self.t > other.t

# class Datum:
#     def __init__(self, value, count, t):
#         self.value = value
#         self.count = count
#         self.t = t

#     def __lt__(self, other):
#         return self.count > other.count or self.count == other.count and self.t > other.t

class FreqStack:
    def __init__(self):
        self.data = []
        self.counts = Counter()
        self.t = 0

    def push(self, x):
        t = self.t
        self.t += 1

        self.counts[x] += 1
        heapq.heappush(self.data, Datum(x, self.counts[x], t))

    def clear_stale_data(self):
        while self.data and self.data[0].count != self.counts[self.data[0].value]:
            heapq.heappop(self.data)

    def pop(self):
        # remove and return most frequent
        # break ties by most recent
        self.clear_stale_data()
        popped = heapq.heappop(self.data)
        self.counts[popped.value] -= 1
        return popped.value

f = FreqStack()
for i in [5, 7, 5, 7, 4, 5]:
    f.push(i)
assert f.pop() == 5
assert f.pop() == 7
assert f.pop() == 5
assert f.pop() == 4

# official solution is stack of stacks: o(1) time everything, no heaps. clever.
