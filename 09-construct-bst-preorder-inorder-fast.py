# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# eleven oh three - eleven twenty six (still failing)
# then I actually pulled up the non-fast version to compare
# eleven twenty nine: done

from david import show

def _reconstruct(preorder, inorder, pi, pj, ii, ij):
    n = pj - pi #+ 1
    if not n:
        return

    root_val = preorder[pi]

    inorder_root_index = inorder.index(root_val, ii, ij)
    lii = ii
    lij = inorder_root_index
    rii = inorder_root_index + 1
    rij = ij

    nl = lij - lii
    lpi = pi + 1
    lpj = pi + nl + 1
    rpi = lpj
    rpj = pj

    left = _reconstruct(preorder, inorder, lpi, lpj, lii, lij)
    right = _reconstruct(preorder, inorder, rpi, rpj, rii, rij)

    return TreeNode(root_val, left, right)

def reconstruct(preorder, inorder):
    return _reconstruct(preorder, inorder, 0, len(preorder), 0, len(inorder))

from david import *
p=1,2,3
i=3,2,1
# t = TreeNode.create((1,2,None,3))
# print(t)
# print(reconstruct((1,2,3),(3,2,1)))

# t = TreeNode.create((1,2,None,3))
# print(t)
# p=[3,9,20,15,7]
# i=[9,3,15,20,7]
print(reconstruct(p, i))
