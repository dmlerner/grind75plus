# https://leetcode.com/problems/invert-binary-tree/
from david import *


def invert(root):
    # swap left and right, return root
    if root is None:
        return
    root.left, root.right = invert(root.right), invert(root.left)
    return root


t = to_tree(-10, 9, 20, None, None, 15, 7)
print(t)
print(invert(t))
