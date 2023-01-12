'''
https://leetcode.com/problems/path-sum-ii/
11:14
11:20 maybe done
11:22 reverse final
11:24 oh its empty...
11:28 92/115 pass
11:29 100/115
11:30 done
To improve this,
avoid repeatedly copying each child path
by passing *down* the recursion
the nodes in the current path.
'''

def get_all_paths(root, target_sum):
    if root is None:
        return []
    child_paths = []
    child_target_sum = target_sum - root.val
    children = tuple(filter(bool, (root.left, root.right)))
    for child in children:
        child_paths.extend(get_all_paths(child, child_target_sum))
    for path in child_paths:
        path.insert(0, root.val)
    if target_sum == root.val and not children:
        child_paths.append([root.val])
    return child_paths

from david import *
t=TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(get_all_paths(t, 22))
