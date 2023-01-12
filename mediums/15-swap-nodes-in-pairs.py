'''
https://leetcode.com/problems/swap-nodes-in-pairs/
11:08
11:13
'''

def swap_in_pairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    # head = a.b.c.d.e
    # d.c.e
    head_of_tail = swap_in_pairs(head.next.next)
    # b.next = a
    head.next.next = head
    # b
    ret = head.next
    # a.next = d.c.e
    head.next = head_of_tail
    return ret

