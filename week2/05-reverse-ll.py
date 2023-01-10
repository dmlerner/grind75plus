# https://leetcode.com/problems/reverse-linked-list/
# 16:12
# 16:17 fml I want a break
# 1449-1612 solved 7 problems
# 83/7 = 11.8min/problem


def reverse(head):
    if head is None or head.next is None:
        return head
    # head # a
    head_of_tail = head.next  # b
    head.next = None
    head_of_reversed_tail = reverse(head_of_tail)  # d -> c -> b
    head_of_tail.next = head  # b.next = a
    return head_of_reversed_tail


def reverse2(head, already_reversed=None):
    if head is None:
        return already_reversed
    new_head = head.next
    head.next = already_reversed
    return reverse2(new_head, head)


def reverse3(head):
    already_reversed = None
    while head:
        new_head = head.next
        head.next = already_reversed
        already_reversed = head
        head = new_head
    return already_reversed


def reverse4(head):
    already_reversed = None
    while head:
        # print(head)
        head.next, head, already_reversed = already_reversed, head.next, head
        # t = head.next, head, already_reversed
        # head, already_reversed, head.next = t
    return already_reversed


# def reverse5(head):
#     already_reversed = None
#     while head:
#         head, head.next, already_reversed = head.next, already_reversed, head

from david import *

ll = ListNode.create((1, 2, 3, 4))
print(ll)
print(reverse4(ll))
