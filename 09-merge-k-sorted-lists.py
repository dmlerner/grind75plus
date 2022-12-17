# https://leetcode.com/problems/merge-k-sorted-lists/
# ten fifty
# eleven twelve done?

from david import ListNode, show

# def verify_list_of_nodes(lon):
#     assert isinstance(lon, list)
#     assert all(l is None or isinstance(l, ListNode) for l in lon)
#     assert all(isinstance(l, ListNode) for l in lon)

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
# print(_merge_recursive(lists[0], lists[1]))
merged = merge(lists)
print(merged)
