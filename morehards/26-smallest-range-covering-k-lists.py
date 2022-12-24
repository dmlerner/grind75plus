# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# 11:29
# 11:43 alright idea

import heapq
import bisect
from dataclasses import dataclass
from david import *

def merge(lists):
    merged = []
    heap = [(l[0], 0, l) for i, l in enumerate(lists)]
    heapq.heapify(heap)
    while heap:
        value, i, l = heapq.heappop(heap)
        merged.append(value)
        try:
            heapq.heappush(heap, (l[i+1], i+1, l))
        except IndexError:
            continue
    return merged


def min_range(lists):
    lower_bound_range = min(l[0] for l in lists), min(l[-1] for l in lists)
    upper_bound_range = max(l[0] for l in lists), max(l[-1] for l in lists)
    merged = merge(lists)
    left = 0
    right = len(lower_bound_range) - 1
    while left <= right:
        middle = (right + left)//2

def better(intervals):
    size = lambda interval: interval[1] - interval[0]
    d1, d2 = map(size, intervals)
    if d1 == d2:
        return min(intervals, key = lambda x: x[0])
    return min(intervals, key=size)

@dataclass
class HeapNode:
    value: int
    value_index: int
    list_index: int
    min_heap: bool

    def __lt__(self, other):
        assert not (self.min_heap ^ other.min_heap)
        if self.min_heap:
            return self.value <= other.value
        return self.value >= other.value

    def get_memo_key(self):
        return self.value_index, self.list_index

def min_range2(lists):
    lower_bounds = [HeapNode(l[0], 0, i, True) for i, l in enumerate(lists)]
    upper_bounds = [HeapNode(l[-1], len(l)-1, i, False) for i, l in enumerate(lists)]
    heapq.heapify(lower_bounds)
    heapq.heapify(upper_bounds)

    def show_heaps():
        debug(f'{lower_bounds =}')
        debug(f'{upper_bounds =}')
    show_heaps()

    smallest = lower_bounds[0].value, upper_bounds[0].value
    memo = {}
    def dfs():
        debug()
        nonlocal smallest
        debug(smallest, len(lower_bounds), len(upper_bounds))
        if not lower_bounds or not upper_bounds:
            return False

        lower_bound = lower_bounds[0]
        upper_bound = upper_bounds[0]
        interval = lower_bound.value, upper_bound.value
        debug(f'{interval =}')
        if interval[0] > interval[1]:
            return False


        memo_key = lower_bound.get_memo_key(), upper_bound.get_memo_key()
        if memo_key in memo:
            return memo[memo_key]
        memo[memo_key] = False

        possible = False

        smallest = better((smallest, interval))
        # if smallest == (20, 22):
        #     breakpoint()
        # try:
        #     assert smallest[0] <= smallest[1]
        # except:
        #     breakpoint()

        list_index = lower_bound.list_index
        value_index = lower_bound.value_index + 1
        if value_index < len(lists[list_index]):
            debug('lower')
            show_heaps()
            possible = True
            heapq.heappop(lower_bounds)
            node = HeapNode(lists[list_index][value_index], value_index, list_index, True)
            debug(f'{node =}')
            if node not in lower_bounds:
                heapq.heappush(lower_bounds, node)
            possible = dfs() or possible
            # popped = heapq.heappop(lower_bounds)
            # debug(f'{popped =}')
            # assert popped is node
            heapq.heappush(lower_bounds, lower_bound)

        list_index = upper_bound.list_index
        value_index = upper_bound.value_index - 1
        if value_index >= 0:
            debug('upper')
            show_heaps()
            possible = True
            heapq.heappop(upper_bounds)
            node = HeapNode(lists[list_index][value_index], value_index, list_index, False)
            debug(f'{node =}')
            heapq.heappush(upper_bounds, node)
            possible = dfs() or possible
            # popped = heapq.heappop(upper_bounds)
            # debug(f'{popped =}')
            # assert popped is node
            heapq.heappush(upper_bounds, upper_bound)

        memo[memo_key] = possible
        return possible



    dfs()
    return smallest




nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
debug.ENABLE = True
print(min_range2(nums))
