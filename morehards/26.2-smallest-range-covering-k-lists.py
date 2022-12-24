from david import *

import heapq
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class HeapNode:
    value: int
    value_index: int
    list_index: int

    def __lt__(self, other):
        return self.value <= other.value

def merge(lists):
    merged = []
    heap = [HeapNode(l[0], 0, i) for i, l in enumerate(lists)]
    heapq.heapify(heap)
    while heap:
        node = heapq.heappop(heap)
        merged.append(node)
        try:
            heapq.heappush(heap, HeapNode(lists[node.list_index][node.value_index+1], node.value_index+1, node.list_index))
        except IndexError:
            continue
    return merged

def better(intervals):
    size = lambda interval: interval[1] - interval[0]
    d1, d2 = map(size, intervals)
    if d1 == d2:
        return min(intervals, key = lambda x: x[0])
    return min(intervals, key=size)

def min_range(lists):
    merged = merge(lists)
    # the *next* element of merged to be added or removed
    i = j = 0
    lists_covered = set()
    count_by_list = defaultdict(int)
    interval = merged[0].value, merged[-1].value
    best = interval
    count = 0

    something = True
    while something:
        something = False

        while j < len(merged) and len(lists_covered) != len(lists):
            something = True
            value, list_index = merged[j].value, merged[j].list_index
            lists_covered.add(list_index)
            count_by_list[list_index] += 1
            interval = interval[0], value
            j += 1

        while len(lists_covered) == len(lists):
            something = True
            value, list_index = merged[i].value, merged[i].list_index
            if value > interval[1]:
                break
            count_by_list[list_index] -= 1
            if count_by_list[list_index] == 0:
                lists_covered.remove(list_index)
            interval = value, interval[1]
            i += 1

        best = better((interval, best))

    return best


lists = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(min_range(lists))
