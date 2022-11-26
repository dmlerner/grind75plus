# https://leetcode.com/problems/min-stack/
# four fifteen - four twenty one


class MinStack:
    def __init__(self):
        self.elements = []
        self.mins = []

    def push(self, val):
        self.elements.append(val)
        if not self.mins and val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self):
        popped = self.elements.pop()
        if popped == self.mins[-1]:
            del self.mins[-1]
        return popped

    def top(self):
        return self.elements[-1]

    def getMin(self):
        return self.mins[-1]
