class MyQueue:
    def __init__(self):
        self.stack_oldest = []
        self.stack_newest = []

    def enqueue(self, value):
        self.stack_newest.append(value)

    def isnewestEmpty(self):
        return len(self.stack_newest) == 0

    def isoldestEmpty(self):
        return len(self.stack_oldest) == 0

    def reversestack(self):
        for i in range(len(self.stack_newest)):
            poped_item = self.stack_newest.pop()
            self.stack_oldest.append(poped_item)

    def dequeue(self):
        if self.isoldestEmpty():
            self.reversestack()
        return self.stack_oldest.pop()

    def peek(self):
        if self.isoldestEmpty():
            self.reversestack()
        return self.stack_oldest[-1]

obj = MyQueue()
obj.enqueue(1)
obj.enqueue(7)
obj.enqueue(8)
print(obj.dequeue())
print(obj.peek())
