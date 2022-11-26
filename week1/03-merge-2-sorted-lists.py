from david import ListNode, show

def merge_simple(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        head = tail = list1
        list1 = list1.next
    else:
        head = tail = list2
        list2 = list2.next


    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            tail = list1
            list1 = list1.next
        else:
            tail.next = list2
            tail = list2
            list2 = list2.next
    tail.next = list1 or list2
    return head

def safe_sorted(lists):
    return list(
        sorted(filter(bool, lists), key=lambda listnode: listnode.val, reverse=True)
    )


def safe_pop(lists):
    try:
        return lists.pop()
    except:
        return None


def merge(list1, list2):
    head = None
    tail = None
    lists = [list1, list2]

    while True:
        lists = safe_sorted(lists)
        smaller = safe_pop(lists)
        if not smaller:
            return head
        lists.append(smaller.next)

        head = head or smaller
        (tail or smaller).next = smaller
        tail = smaller

    return head

def merge_recursive(list1, list2, head=None, tail=None):
    lists = list(filter(bool, (list1, list2)))
    if len(lists) == 1:
        if tail:
            tail.next = next(filter(bool, (list1, list2)))
        return head or list1 or list2

    if len(lists) == 2:
        argmin = list1.val > list2.val
        min = lists[argmin]
        lists[argmin] = min.next

        head = head or min
        if tail:
            tail.next = min
        return merge_recursive(*lists, head, min)

def merge_recursive_match(list1, list2, head=None, tail=None):
    lists = list(filter(bool, (list1, list2)))
    match lists:
        case []:
            return
        case [a]:
            if tail:
                tail.next = a
            return head or a
        case lists:
            argmin = list1.val > list2.val
            min = lists[argmin]
            lists[argmin] = min.next

            head = head or min
            if tail:
                tail.next = min
            return merge_recursive(*lists, head, min)
# l1 = ListNode.create(1, 4, 6)
# print(l1)
# l2 = ListNode.create(2, 5, 7)
# print(l2)
# l3 = merge_simple(l1, l2)
# print(l3)


l1 = ListNode.create(1,1.5)
print(l1)
l2 = ListNode.create(0, 2)
print(l2)
l3 = merge_recursive(l1, l2)
print(l3)
