'''
https://leetcode.com/problems/maximum-width-of-binary-tree/
1:20
1:36 passes
1:37 cheat a little, realize dfs should work
1:41 implemented, but slow???
'''
from david import *

from dataclasses import dataclass

'''
@dataclass
class TreeNodePosition:
    node: TreeNode
    layer: int
    index: int

    def get_left(self):
        if not self.node.left:
            return
        return TreeNodePosition(self.node.left, self.layer+1, self.index*2)

    def get_right(self):
        if not self.node.right:
            return
        return TreeNodePosition(self.node.right, self.layer+1, self.index*2+1)

    def get_children(self):
        return list(filter(bool, (self.get_left(), self.get_right())))

def get_max_width(root):
    max_width = 0
    for first, last in bfs_coordinates(root):
        width = last.index - first.index + 1
        max_width = max(max_width, width)
    return max_width


def bfs_coordinates(root):
    layer = 0
    previous_layer = [TreeNodePosition(root, 0, 0)]
    current_layer = []

    while previous_layer:
        yield previous_layer[0], previous_layer[-1]
        for p in previous_layer:
            current_layer.extend(p.get_children())
        previous_layer = current_layer
        current_layer = []
'''
def dfs_coordinates(root, layer=0, index=0):
    if not root:
        return
    yield layer, index
    yield from dfs_coordinates(root.left, layer+1, index*2)
    yield from dfs_coordinates(root.right, layer+1, index*2+1)

def get_max_width_dfs(root):
    max_width = 0
    min_index_by_layer = {}
    max_index_by_layer = {}
    for layer, index in dfs_coordinates(root):
        min_index_by_layer.setdefault(layer, index)
        max_index_by_layer[layer] = index

    for layer in min_index_by_layer:
        width = max_index_by_layer[layer] - min_index_by_layer[layer] + 1
        max_width = max(max_width, width)
    return max_width





clean()

