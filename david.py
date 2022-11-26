class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"LN({self.val}|{self.next})"

    @staticmethod
    def create(vals):
        if not vals:
            return None
        head = ListNode(vals[-1])
        for v in reversed(vals[:-1]):
            head = ListNode(v, head)
        return head


def show(f):
    def _f(*args):
        print(f.__name__, *args)
        ret = f(*args)
        print(f.__name__, *args, "=", ret)
        print()
        return ret

    return _f


def is_leaf(node):
    return node.left is None and node.right is None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if is_leaf(self):
            return f"L({self.val})"
        lchild = "{" + str(self.left) + "}"
        rchild = "{" + str(self.right) + "}"
        return f"T({self.val}{lchild}{rchild})"
        # return f"T({self.val}[\{{self.left}\}|\{{self.right}\}])"

    @staticmethod
    def create(vals):
        root_node = TreeNode(vals[0])
        nodes = [root_node]
        i = 0
        left = False
        for v in vals[1:]:
            left = not left
            node = TreeNode(v) if v is not None else None
            while nodes[i] is None:
                i += 1
            if left:
                nodes[i].left = node
            else:
                nodes[i].right = node
                i += 1
            nodes.append(node)
        return root_node


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"G({self.val}, {len(self.neighbors)})"
