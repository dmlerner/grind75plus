from david import *

NULL = 'NULL'
UNSET_NODE = TreeNode(None)

def serialize(root):
    if not root:
        yield NULL
        return
    yield str(root.val)
    yield from serialize(root.left)
    yield from serialize(root.right)

def make_node_with_null_children(val):
    return TreeNode(int(val), UNSET_NODE, UNSET_NODE)

def deserialize(serialized_generator):
    root = make_node_with_null_children(next(serialized_generator))
    stack = [root]
    for token in serialized_generator:
        assert stack
        last = stack[-1]
        t = None
        if token != NULL:
            t = make_node_with_null_children(token)
        if last.left is UNSET_NODE:
            last.left = t
        else:
            last.right = t
            stack.pop()
        if t:
            stack.append(t)
    return root

t = TreeNode.create((1,2,3,4))
ds = deserialize(serialize(t))
assert t == ds
