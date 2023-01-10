# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
from david import *
from collections import defaultdict


def find(root, val, ancestors):
    if root is None:
        return None
    if root.val == val:
        return root
    if val < root.val:
        found = find(root.left, val, ancestors)
    else:
        found = find(root.right, val, ancestors)
    if found is None:
        return None
    ancestors[val].add(found)


# @show
def get_path(root, val):
    yield root

    if root.val == val:
        return

    next_root = root.left if val < root.val else root.right
    yield from get_path(next_root, val)


# @show
def get_lca(root, p, q):
    # this assumed p and q are values, not treenodes
    paths = map(lambda x: get_path(root, x), (p, q))
    lca = root
    for (p_anc, q_anc) in zip(*paths):
        if p_anc is not q_anc:
            break
        lca = p_anc
    return lca


root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = 2
q = 4
# root = [2, 1]
t = TreeNode.to_tree(root)
print(f"{t=}")
# breakpoint()
lca = get_lca(t, p, q)
print(f"{lca=}")
