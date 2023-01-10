"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
7:02
7:05 almost right
7:06 almoster (180/208)
7:08 done
"""


def remove_nth_from_end(head, n):
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
