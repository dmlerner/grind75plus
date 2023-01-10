class MyQueue:
    def __init__(self):
        self.lifo = []

    def push(self, x):
        self.lifo.append(x)

    @staticmethod
    def reverse(x):
        reversed = []
        while x:
            reversed.append(x.pop())
        return reversed

    def pop(self):
        fifo = MyQueue.reverse(self.lifo)
        popped = fifo.pop()
        self.lifo = MyQueue.reverse(fifo)
        return popped

    def peek(self):
        fifo = MyQueue.reverse(self.lifo)
        peeked = fifo[-1]
        self.lifo = MyQueue.reverse(fifo)
        return peeked

    def empty(self):
        return not bool(self.lifo)
