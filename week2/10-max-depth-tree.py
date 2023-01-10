from david import *


def max_depth(t):
    if t is None:
        return 0
    return 1 + max(0, *map(max_depth, (t.left, t.right)))
