from david import TreeNode

t = TreeNode.create(
    [
        4,
        -7,
        -3,
        None,
        None,
        -9,
        -3,
        9,
        -7,
        -4,
        None,
        6,
        None,
        -6,
        -6,
        None,
        None,
        0,
        6,
        5,
        None,
        9,
        None,
        None,
        -1,
        -4,
        None,
        None,
        None,
        -2,
    ]
)
print(t)

from functools import cache

# count edges
@cache
def diameter(t):
    if t is None:
        return 0
    longest_path_using_t = sum(map(longest_one_sided, (t.left, t.right)))
    return max(longest_path_using_t, *map(diameter, (t.left, t.right)))


# count of nodes
@cache
def longest_one_sided(t):
    if t is None:
        return 0
    longest_left = longest_one_sided(t.left)
    longest_right = longest_one_sided(t.right)
    return 1 + max(longest_left, longest_right)


def diameter_and_longest_one_sided(t):
    if t is None:
        return -1, 0
    (ld, los), (rd, ros) = map(diameter_and_longest_one_sided, (t.left, t.right))
    return max(ld, rd, los + ros), max(los, ros) + 1


def diameter2(t):
    return diameter_and_longest_one_sided(t)[0]


print(diameter(t))
# T(4[ L(-7)|T(-3[ T(-9[ T(9[ T(6[ T(0[ None|L(-1) ])|T(6[ L(-4)|None ]) ])|None ])|T(-7[ T(-6[ L(5)|None ])|T(-6[ T(9[ L(-2)|None ])|None ]) ]) ])|T(-3[ L(-4)|None ]) ]) ])
# T(4{L(-7)}{T(-3{T(-9{T(9{T(6{T(0{None}{L(-1)})}{T(6{L(-4)}{None})})}{None})}{T(-7{T(-6{L(5)}{None})}{T(-6{T(9{L(-2)}{None})}{None})})})}
# {T(-3{L(-4)}{None})})})
