# https://leetcode.com/problems/clone-graph/
# eleven twenty one - eleven twenty two (with copy)
# eleven twenty two - eleven thirty seven

import copy
from david import *


def clone(node):
    return copy.deepcopy(node)


from collections import deque


def clone2(node):
    if not node:
        return

    copy_by_original = {node: Node(node.val)}
    seen_original_nodes = set()
    frontier = deque([node])  # originals

    while frontier:
        active_original_node = frontier.popleft()

        for neighbor in active_original_node.neighbors:
            if neighbor not in seen_original_nodes:
                seen_original_nodes.add(neighbor)
                frontier.append(neighbor)
                copy_by_original[neighbor] = Node(neighbor.val)

            copy_by_original[active_original_node].neighbors.append(
                copy_by_original[neighbor]
            )
    return copy_by_original[node]
