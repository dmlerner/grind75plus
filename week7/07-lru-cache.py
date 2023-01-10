# three fourty eight
# four sixteen
class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        # no need to update self


class LinkedList:
    def __init__(self):
        self.head = LinkedListNode()  # least recently used
        self.tail = LinkedListNode()  # most
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, lln):
        last_non_tail_node = self.tail.prev

        last_non_tail_node.next = lln
        lln.next = self.tail

        lln.prev = last_non_tail_node
        self.tail.prev = lln

    def pop(self):
        first_non_head_node = self.head.next
        self.head.next = first_non_head_node.next
        first_non_head_node.next.prev = self.head

        return first_non_head_node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pairs = {}
        self.use_order = LinkedList()
        self.use_node_by_key = {}

    def put(self, k, v):
        # if k == 3:
        #     breakpoint()
        if k not in self.pairs:
            if len(self.pairs) == self.capacity:
                self.evict()
        self.pairs[k] = v
        self.record_use(k)

    def get(self, k):
        if k not in self.pairs:
            return -1
        self.record_use(k)
        return self.pairs[k]

    def record_use(self, k):
        assert k in self.pairs
        if k in self.use_node_by_key:
            self.use_node_by_key[k].remove()
        use_node = LinkedListNode(k)
        self.use_order.push(use_node)
        self.use_node_by_key[k] = use_node

    def evict(self):
        k = self.use_order.pop().value
        del self.pairs[k]
        del self.use_node_by_key[k]


actions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
lru = None
for (action, arg) in zip(actions, args):
    print(action, arg)
    if action == "LRUCache":
        lru = LRUCache(*arg)
    if action == "put":
        lru.put(*arg)
    if action == "get":
        print(lru.get(*arg))
    print(lru.pairs)
    print()
