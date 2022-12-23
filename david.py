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
    @wraps(f)
    def _f(*args, **kwargs):
        print(f.__name__, *args, *kwargs.items())
        ret = f(*args, **kwargs)
        print(f.__name__, *args, *kwargs.items(), "->", ret)
        return ret

    return _f


def count_calls(f):
    def _f(*args, **kwargs):
        _f.call_count += 1
        return f(*args, **kwargs)

    _f.call_count = 0

    def reset_call_count():
        _f.call_count = 0

    _f.reset_call_count = reset_call_count
    return _f


def is_leaf(node):
    return node.left is None and node.right is None


def assert_null_or_same_type(a, b):
    if a is None or b is None:
        return
    assert type(a) is type(a)


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

    def __eq__(self, other):
        if other is None:
            return self is None
        assert isinstance(other, TreeNode)
        assert_null_or_same_type(self.val, other.val)
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

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


from functools import wraps
import inspect


def show_locals(n=1):
    frame = inspect.currentframe()
    for i in range(n):
        frame = frame.f_back
    print('\n'.join(map(str, frame.f_locals.items())))
    print()
sl = show_locals

# def recursion_limit(n=10):
#     def decorator(f):
#         count = 0

#         @wraps(f)
#         def _f(*args):
#             nonlocal count
#             assert count < n
#             count += 1
#             return f(*args)

#         return _f

#     return decorator

class InfiniteRecursionException(Exception):
    pass

def recursion_limit(f):
    memo = {}
    @wraps(f)
    def _f(*args, **kwargs):
        key = args, tuple(kwargs.items())
        if key in memo and memo[key] is None:
            raise InfiniteRecursionException()
        memo[key] = None
        ret = f(*args, **kwargs)
        memo[key] = ret
        return ret
    return _f


def listify(f):
    @wraps(f)
    def _f(*args, **kwargs):
        return list(f(*args, **kwargs))

    return _f

def showlistify(f):
    @show
    @listify
    @wraps(f)
    def _f(*args, **kwargs):
        return f(*args, **kwargs)
    return _f

import time
def benchmark(f):
    start = time.time()
    ret = f()
    stop = time.time()
    return stop - start, ret

