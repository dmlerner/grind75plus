from david import TreeNode
# https://leetcode.com/problems/binary-tree-level-order-traversal/

def level_order(root):
    if not root:
        return []
    values = []

    last_level = [root]
    while last_level:
        values.append(list(map(lambda t: t.val, last_level)))

        active_level = []
        for node in last_level:
            children = filter(bool, (node.left, node.right))
            active_level.extend(list(children))

        last_level = active_level
    return values

t = TreeNode.create([3,9,20,None,None,15,7])
print(t)
print(level_order(t))
