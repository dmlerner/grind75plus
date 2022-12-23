# https://leetcode.com/problems/sliding-window-maximum/
# 6:52
# 7:10 done
# ah, could have done it without a heap! classic monoqueue problem, and not a "really a stack" one.

import heapq
from collections import deque, Counter

class MaxHeap:
    def __init__(self, k):
        self.heap = []
        self.queue = deque([])
        self.counts = Counter()
        self.k = k

    def push(self, x):
        heapq.heappush(self.heap, -x)
        self.queue.append(x)
        self.counts[x] += 1
        if len(self.heap) > self.k:
            self.counts[self.queue.popleft()] -= 1

    def get_max(self):
        while self.counts[-self.heap[0]] == 0:
            heapq.heappop(self.heap)
        return -self.heap[0]

def max_sliding_window(nums, k):
    h = MaxHeap(k)
    nums = iter(nums)
    for i in range(k):
        h.push(next(nums))
    yield h.get_max()
    for num in nums:
        h.push(num)
        yield h.get_max()

class Solution:
    def maxSlidingWindow(self, nums, k):
        return list(max_sliding_window(nums, k))

w = list(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(w)
assert w == [3, 3, 5, 5, 6, 7]
