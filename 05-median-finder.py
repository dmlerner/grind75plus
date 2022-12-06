# https://leetcode.com/problems/find-median-from-data-stream/
# eight twenty eight - eight fifty two

from david import show

import heapq
from itertools import starmap
import operator

class MinHeap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key = key

    def push(self, x):
        heapq.heappush(self.data, (self.key(x), x))

    def peek(self):
        return self.data[0][1]

    def pop(self):
        return heapq.heappop(self.data)[1]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

class MaxHeap(MinHeap):
    def __init__(self, key=lambda x:x):
        super().__init__(lambda x: -key(x))

class MedianFinder:
    def __init__(self):
        self.above_median = MinHeap()
        self.below_median = MaxHeap()

    def __len__(self):
        return len(self.above_median) + len(self.below_median)

    def findMedian(self):
        heaps = self.get_heaps()
        if len(self) % 2:
            return max(heaps, key=len).peek()
        return sum(h.peek() for h in heaps)/2

    def addNum(self, num):
        if not len(self):
            self.below_median.push(num)
            return
        median = self.findMedian()
        heap = self.get_heaps()[num > median]
        heap.push(num)
        self.balance_heaps()

    def get_heaps(self):
        return [self.below_median, self.above_median]

    def balance_heaps(self):
        heaps = self.get_heaps()
        heaps.sort(key=len)
        if abs(len(heaps[1]) - len(heaps[0])) > 1:
            heaps[0].push(heaps[1].pop())

    def __repr__(self):
        return f'{self.below_median}, {self.above_median}, {self.findMedian()}'

m = MedianFinder()
# print(m)
for i in range(10):
    m.addNum(i)
    print(m)
