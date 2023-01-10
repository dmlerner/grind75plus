# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 10:04

from david import TreeNode
from functools import cache

TreeNode.__hash__ = lambda t: hash(id(t))


def get_children(t):
    return list(filter(bool, (t.left, t.right)))


@cache
def max_path_sum_one_sided(t):
    # must take t
    if not (
        positive_children := list(
            filter(lambda x: x > 0, map(max_path_sum_one_sided, get_children(t)))
        )
    ):
        return t.val
    return t.val + max(positive_children)


@cache
def max_path_sum(t):
    # may take t, must take something
    if not (children := get_children(t)):
        return t.val

    child_max_path_one_sided = tuple(map(max_path_sum_one_sided, children))
    positive_child_max_path_one_sided = tuple(
        filter(lambda x: x > 0, child_max_path_one_sided)
    )
    child_max_path_sum = tuple(map(max_path_sum, children))

    return max(
        t.val, max(child_max_path_sum), t.val + sum(positive_child_max_path_one_sided)
    )


#     m = 0

#     if t.val >= 0:
#         m += t.val
#         if positive_children:
#             m += sum(positive_children)
#     else:

#         return t.val + sum(positive_children)
#     return max(max(postive_children), t.val + sum(positive_children))


t = TreeNode.create([-10, 9, 20, None, None, 15, 7])
t = TreeNode.create([1, 2, 3])
t = TreeNode.create([-1])
t = TreeNode.create([-10, 9, 20, None, None, 15, 7])

print(t)
print(max_path_sum(t))
