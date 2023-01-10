"""
https://leetcode.com/problems/graph-valid-tree/
7:51
7:59 algorithm idea
8:03 implemented idea
8:05 oh god that's not right
8:11 correct
"""

from collections import defaultdict


def valid_tree(n, edges):
    if n != len(edges) + 1:
        return False

    neighbors_by_node = defaultdict(set)
    for (a, b) in edges:
        neighbors_by_node[a].add(b)
        neighbors_by_node[b].add(a)

    arbitrary_start_node = 0
    in_stack = set((arbitrary_start_node,))
    visited = set((arbitrary_start_node,))
    stack = [arbitrary_start_node]

    while stack:
        active = stack.pop()
        in_stack.remove(active)
        visited.add(active)

        for neighbor in neighbors_by_node[active]:
            if neighbor in in_stack:
                return False

            if neighbor not in visited:
                in_stack.add(neighbor)
                stack.append(neighbor)

    return len(visited) == n


edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(valid_tree(5, edges))
