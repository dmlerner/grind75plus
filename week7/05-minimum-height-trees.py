# https://leetcode.com/problems/minimum-height-trees/
# seven on nine
# seven sixteen start programming
# seven fourty passing

from collections import defaultdict, deque


def get_mht_roots(n, edges):
    if n == 1:
        return [0]
    # no need for n...
    neighbors_by_node = defaultdict(set)
    for (n1, n2) in edges:
        neighbors_by_node[n1].add(n2)
        neighbors_by_node[n2].add(n1)

    frontier = None
    # print(frontier)
    next_level = [n for (n, ns) in neighbors_by_node.items() if len(ns) == 1]
    prev_level = []
    while frontier or next_level:
        if not frontier:
            print(next_level)
            prev_level = next_level
            frontier = deque(next_level)
            next_level = []

        active = frontier.popleft()
        # print(active, next_level, prev_level)
        if not neighbors_by_node[active]:
            return prev_level or next_level
        neighbor = neighbors_by_node[active].pop()
        neighbors_by_node[neighbor].remove(active)
        if len(neighbors_by_node[neighbor]) == 1:
            next_level.append(neighbor)
        del neighbors_by_node[active]


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

n = 2
edges = [[0, 1]]
get_mht_roots(n, edges)
