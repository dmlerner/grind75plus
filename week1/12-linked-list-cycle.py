def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow and fast and fast.next and slow is not fast:
        slow = slow.next
        fast = fast.next.next
    return slow is fast


