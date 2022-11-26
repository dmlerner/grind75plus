# https://leetcode.com/problems/time-based-key-value-store/
# one twenty - one thirty two
# I missed the note that set will be called with increasing times only
# which is worst case for a tree
class TreeNode:
    def __init__(self, v, timestamp):
        self.v = v
        self.timestamp = timestamp
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def add(self, other):
        # if other is self:
        #     return

        if other < self:
            if self.left:
                self.left.add(other)
            else:
                self.left = other
        else:
            if self.right:
                self.right.add(other)
            else:
                self.right = other

    def get(self, timestamp):
        if timestamp == self.timestamp:
            return self
        elif timestamp > self.timestamp:
            if not self.right:
                return self
            return self.right.get(timestamp) or self
        if self.left:
            return self.left.get(timestamp)


class TimeMap:
    def __init__(self):
        self.value_tree_by_key = {}

    def set(self, k, v, timestamp):
        tree_node = TreeNode(v, timestamp)
        if k not in self.value_tree_by_key:
            self.value_tree_by_key[k] = tree_node
        else:
            self.value_tree_by_key[k].add(tree_node)

    def get(self, k, timestamp):
        if k not in self.value_tree_by_key:
            return ""
        tree_node = self.value_tree_by_key[k].get(timestamp)
        if not tree_node:
            return ""
        return tree_node.v
