# https://leetcode.com/problems/merge-k-sorted-lists/
# ten fifty
# eleven twelve done?

from david import ListNode, show


@show
# Broken
def _merge(a, b):
    if not (a and b):
        return a or b

    merged = None
    nodes = (a, b)
    while True:
        nodes = tuple(filter(bool, nodes))
        print(nodes, merged)
        if len(nodes) == 1:
            merged.next = nodes[0]
            break
        smaller, larger = sorted(nodes, key=lambda n: n.val)
        if merged is None:
            merged = smaller
        else:
            merged.next = smaller
            merged = merged.next
        nodes = (smaller.next, larger)
        # merged.next = None
    return merged


def merge(lists):
    # verify_list_of_nodes(lists)
    if len(lists) <= 1:
        return lists
    if len(lists) == 2:
        return [_merge_recursive(*lists)]
    left_merged = merge(lists[: len(lists) // 2])
    # verify_list_of_nodes(left_merged)
    right_merged = merge(lists[len(lists) // 2 :])
    # verify_list_of_nodes(right_merged)
    return merge(left_merged + right_merged)


def _merge_recursive(a, b):
    if not (a and b):
        return a or b
    if a.val > b.val:
        return _merge_recursive(b, a)

    tail_merge = _merge_recursive(a.next, b)
    a.next = tail_merge
    return a


lists = list(map(ListNode.create, [[1, 4, 5], [1, 3, 4], [2, 6]]))
print(lists)
# print(_merge(lists[0], lists[1]))
merged = merge(lists)
print(merged)
