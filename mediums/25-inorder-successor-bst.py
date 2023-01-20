'''
https://leetcode.com/problems/inorder-successor-in-bst/
6:51
8:01 well that's embarassing but also goreous
'''

from david import *


def in_order(root, node):
    ancestors = []
    # get to node
    active = root
    while active is not node:
        if active is None:
            return
        ancestors.append(active)

        if active.val < node.val:
            active = active.right
        else:
            active = active.left
    # follow parent pointers until active has a right child
    while ancestors and ancestors[-1].right is None:
        if ancestors[-1].left is node:
            return ancestors[-1]
        ancestors.pop()
    active = ancestors[-1]
    if active.left is node:
        return active
    active = active.right

    # go left maximally
    while active.left:
        active = active.left

    if active is node:
        return None
    return active

found_node = False
def in_order2(root, node):
    global found_node
    # if successor to node is in subtree rooted at root,
    # but I can't know this...
    # if node is in subtree rooted in left subtree
    # traverse it in order (lazily)
    # ditto right
    if root is node:
        found_node = True

    if not found_node:
        # Just keep going towards the node
        if root.left.val > node.val:
            yield from in_order2(root.left, node)
            assert found_node
            return root
        else:
            yield from in_order2(root.right, node)
            assert found_node

def in_order3(root, node):
    if root is None:
        return
    if root.val > node.val:
        yield from in_order3(root.left, node)
        yield root
    yield from in_order3(root.right, node)

def in_order4(root, node):
    try:
        return next(in_order3(root, node))
    except StopIteration:
        return

def test2():
    t = TreeNode.create([2,1,3])
    print(in_order4(t, t.left))
test2()

def test1():
    t = TreeNode.create([5,3,6,2,4,None, None, 1])
    '''
    T(5
      {T(3
         {T(2
            {L(1)}
            {None})}
         {L(4)})}
      {L(6)}
      )
    '''
    print(t)
    node = t.left.left
    # print(node)
    # print(list(in_order3(t, node)))
    # print(in_order4(t, node))
    nodes = [t.left.left.left, t.left.left, t.left, t.left.right, t, t.right]
    for i in range(5):
        print()
        print(f'{i=}')
        actual = in_order4(t, nodes[i]).val
        expected = nodes[i+1].val
        if actual != expected:
            print('X', nodes[i].val, actual, expected)
        else:
            print(':)')
    print(in_order4(t, nodes[-1]))


