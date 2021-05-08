#space efficient
#use additional stack to keep track of the mins

import sys
class StackWithMin:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def isEmpty(self):
        return len(self.s1) == 0

    def getmin(self):
        if len(self.s2) == 0:
            return sys.maxsize
        else:
            return self.s2[-1]

    def push(self, value):
        if value <= self.getmin():
            self.s2.append(value)
        self.s1.append(value)

    def pop(self):
        poped_value = self.s1.pop()
        if poped_value == self.getmin():
            self.s2.pop()

obj = StackWithMin()
obj.push(7)
obj.push(5)
obj.push(6)
obj.push(1)
print(obj.getmin())
obj.pop()
print(obj.getmin())