# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# one oh one - one sixteen
def get_lca(root, p, q):
    # all inputs are treenodes
    # tree, not bst
    parent_by_node = {}
    depth_by_node = {root: 0}
    def dfs(node):
        if p in parent_by_node and q in parent_by_node:
            return

        children = list(filter(bool, (node.left, node.right)))
        for child in children:
            parent_by_node[child] = node
            depth_by_node[child] = depth_by_node[node] + 1
            dfs(child)

    def get_ancestors(node):
        yield node
        while node in parent_by_node:
            p = parent_by_node[node]
            yield p
            node = p

    dfs(root)

    print(f'{depth_by_node=}')
    shallow, deep = sorted((p, q), key=depth_by_node.get)
    shallow_ancestors = set(get_ancestors(shallow))
    for node in get_ancestors(deep):
        if node in shallow_ancestors:
            return node




from david import *
t = TreeNode.create([3,5,1,6,2,0,8,None,None,7,4])
p=t.left
q=t.right
print(get_lca(t, p, q))
