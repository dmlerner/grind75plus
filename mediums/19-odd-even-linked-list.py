"""
https://leetcode.com/problems/odd-even-linked-list/
7:35
8:03 passes but butt ugly
"""

from david import *


def odd_even(head, even=None, odd=None):
    if head is None or head.next is None:
        return head
    if even is None:
        even = head
    else:
        even.next = head
    if odd is None:
        odd = head.next
    else:
        odd.next = head.next
    odd_even(head, even, odd)
    return head


def odd_even(head):
    if head is None or head.next is None:
        return head

    # 0
    # even = head
    even_tail = head
    # 1
    odd = head.next
    odd_tail = head.next

    """
    happy path
        both even_tail.next and odd_tail.next are not None
    odd_tail.next truthy, even_tail.next none
        extend only even, then return
    both none
        return
    """

    # while even_tail.next or odd_tail.next:
    while True:
        # 1.next = 2
        if odd_tail.next:
            # 0.next = 2
            even_tail.next = odd_tail.next
            # = 2
            even_tail = even_tail.next
        else:
            break
        if even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
        else:
            odd_tail.next = None
            break

    even_tail.next = odd
    return head


l = ListNode.create(range(1, 9))
l = ListNode.create(range(0, 5))
