# https://leetcode.com/problems/validate-binary-search-tree/
# four twenty one - four thirty five
from david import *

# def is_valid(root, gt=float('-inf'), lt=float('inf')):
#     if root is None:
#         return True
#     if root.left and root.left.val >= root.val: # TODO: remove?
#         return False
#     if root.right and root.right.val <= root.val:
#         return False
#     if not (gt <= root.val <= lt):
#         return False
#     left_valid = is_valid(root.left, gt, root.val)
#     right_valid = is_valid(root.right, root.val, lt)
#     return left_valid and right_valid

# t = TreeNode.create([3,1,5,0,2,4,6,None,None,None,3])
# print(t)
# print(is_valid(t))


def is_valid(root, gt=float("-inf"), lt=float("inf")):
    if root is None:
        return True
    if not (gt < root.val < lt):
        return False
    return is_valid(root.left, gt, root.val) and is_valid(root.right, root.val, lt)


t = TreeNode.create((1, None, 1))
print(t)
print(is_valid(t))
