# https://leetcode.com/problems/reverse-nodes-in-k-group/
# 1:25

from david import *


def reverse(head):
    match head:
        case None:
            return None
        case ListNode(val=v, next=None):
            return head
        case ListNode(val=v, next=n):
            head_of_reversed_tail = reverse(n)
            n.next = head
            head.next = None
            return head_of_reversed_tail


def reverse2(head):
    if head is None:
        return None
    if head.next is None:
        return head
    hort = reverse2(head.next)
    # work?
    head.next.next = head
    head.next = None
    return hort


class TooSmallToReverseException(Exception):
    pass


@show
def reverse_group(group_head, reversed_head, reversed_tail, k):
    """reverses the first k elements, returning the first and last of them"""
    # 0, None, None, 3
    # 1, 0, 0, 2
    # 2, 1, 0, 1
    if k == 0:
        return reversed_head, reversed_tail.next
    if group_head is None:
        raise TooSmallToReverseException
    new_reversed_head = group_head  # 0; 1; 2
    new_group_head = group_head.next  # 1; 2; 3
    new_reversed_head.next = reversed_head  # 0.next = None; 1.next = 0; 2.next = 1
    return reverse_group(
        new_group_head, new_reversed_head, reversed_tail or group_head, k - 1
    )


@show
def reverse_groups(head, k):
    """
    a..bc..d with a..b a k-group and c..d a k-group
    b..ad..c
    """
    try:
        # b, a
        # 2, 0
        group_reversed_head, group_reversed_tail = reverse_group(head, None, None, k)
        sl()
    except TooSmallToReverseException:
        return head
    # d, c
    reversed_head, reversed_tail = reverse_groups(group_reversed_head.next, k)
    # a.next = d
    group_reversed_tail.next = reversed_head
    return reversed_head, reversed_tail


def lc(head, k):
    return reverse_groups(head, k)[0]


l = ListNode.create(range(8))
print(l)
print(reverse_groups(l, 3))
# fuck this
