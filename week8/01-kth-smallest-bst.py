# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# twelve ten - twelve nineteen
from functools import cache


def kth_smallest_value(root, k):
    ks = kth_smallest(root, k)
    if ks:
        return ks.val


@cache
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


def kth_smallest(root, k):
    if not root:
        return
    if root.left and size(root.left) >= k:
        return kth_smallest(root.left, k)
    if size(root.left) + 1 == k:
        return self
    return kth_smallest(root.right, k - size(root.left) - 1)
