import heapq
from david import *

def f(nums):
    heap = []
    max_ = 0
    for i, num in enumerate(nums):
        heapq.heappush(heap, (num[0], i, 1))
        max_ = max(num[0], max_)


    a, b = heap[0][0], max_
    sl()
    while 1:
        min_, i, next_j = heapq.heappop(heap)
        if max_ - min_ < b - a:
            debug('update')
            a = min_
            b = max_

        if len(nums[i]) <= next_j:
            break
        max_ = max(nums[i][next_j], max_)
        heapq.heappush(heap, (nums[i][next_j], i, next_j+1))
        sl()

    return [a, b]

lists = [[4,10,15,24,26],[0,9,12,15,20],[5,15,18,22,30]]
lists = [[4,15,16],[0,15,18],[3,15,17]]
print(f(lists))
