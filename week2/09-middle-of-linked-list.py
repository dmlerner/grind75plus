# https://leetcode.com/problems/middle-of-the-linked-list/
from david import *


def reversed_generator(head):
    if head.next is not None:
        yield from reversed_generator(head.next)
    # print('rev', head)
    yield head


def generator(head):
    # print('gen', head)
    yield head
    if head.next is not None:
        yield from generator(head.next)


def middle(head):
    last_forward = None
    for forward, reverse in zip(generator(head), reversed_generator(head)):
        if reverse is forward or reverse is last_forward:
            return forward
        last_forward = forward


ll = ListNode.create(range(1, 6))
print(ll)
print(middle(ll))

ll = ListNode.create(range(1, 7))
print(ll)
print(middle(ll))
