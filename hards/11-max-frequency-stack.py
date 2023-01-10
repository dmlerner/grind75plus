# https://leetcode.com/problems/maximum-frequency-stack/
# 12:09
# twelve eighteen ugh I guess I'm writing a heap


class HeapNode:
    def __init__(self, value, key=lambda node: node.value):
        self.value = value
        self.key = key

    def __ge__(self, other):
        return self.key(self) >= other.key(other)

    def __hash__(self):
        return hash(id(self))


class MinHeap:
    # TODO; recusive minheap?
    def __init__(self, key=lambda node: node.value):
        self.nodes = []
        self.index_by_node = {}
        self.key = key

    @staticmethod
    def parent(i):
        return i // 2

    @staticmethod
    def lchild(i):
        return 2 * i + 1

    @staticmethod
    def rchild(i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.index_by_node[self.nodes[i]] = j
        self.index_by_node[self.nodes[j]] = i
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def satisfies_invariant(self, i):
        return i == 0 or self.nodes[i] >= self.nodes[MinHeap.parent(i)]

    def push(self, x):
        self.nodes.append(HeapNode(x, self.key))
        self._heapify()

    def _heapify(self):
        i = len(self.nodes) - 1
        while not self.satisfies_invariant(i):
            parent = MinHeap.parent(i)
            self._swap(i, parent)
            i = parent

    def delete(self, node):
        index = self.index_by_node[node]
        self.swap(index, -1)
        del self.nodes[-1]
        self._heapify()

    def pop(self):
        popped = self.nodes[0]
        self._swap(0, -1)
        del self.nodes[-1]
        self._heapify()
        return popped.value

    def check(self):
        for i in range(len(self.nodes)):
            assert self.satisfies_invariant(i)


h = MinHeap()
h.check()
h.push(2)
h.check()
h.push(1)
h.check()
assert h.pop() == 1
h.check()


import heapq
from collections import Counter


class FreqStack:
    def __init__(self):
        # self.frequency_heap = MinHeap(lambda node:
        self.nodes = []
        self.counts = Counter()

    def push(self, x):
        pass

    def pop(self):
        # remove and return most frequent
        # break ties by most recent
        pass
