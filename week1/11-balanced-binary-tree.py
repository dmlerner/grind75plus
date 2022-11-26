from david import TreeNode

def height(t):
    if not t:
        return 0

    left_height = height(t.left) if t.left else 0
    right_height = height(t.right) if t.right else 0
    return 1 + max(left_height, right_height)

def is_balanced(t):
    if not t:
        return True
    if not abs(height(t.left)-height(t.right)) <= 1:
       return False
    return is_balanced(t.left) and is_balanced(t.right)

t = TreeNode.to_tree((1,2,2,3,3,None,None,4,4))
print(t)
print(is_balanced(t))
