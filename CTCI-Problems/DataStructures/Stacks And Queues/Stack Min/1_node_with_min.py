#not space efficient
#waste lot of space by keeping track of min for every single element
import sys
class NodeWithMin:
    def __init__(self, value, min):
        self.value = value
        self.min = min

    def __str__(self):
        return str(self.value)

class StackWithMin:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        if value <= self.getmin():
            min = value
        else:
            min = self.getmin()
        new_node = NodeWithMin(value, min)
        self.stack.append(new_node)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            self.stack.pop()

    def getmin(self):
        if len(self.stack) == 0:
            return sys.maxsize
        else:
            return self.peek().min

    def peek(self):
        return self.stack[-1]

    def printstack(self):
        for i in self.stack:
            print(i)

obj = StackWithMin()
obj.push(7)
obj.push(4)
obj.push(6)
obj.push(1)
print(obj.getmin())
obj.pop()
print(obj.getmin())
