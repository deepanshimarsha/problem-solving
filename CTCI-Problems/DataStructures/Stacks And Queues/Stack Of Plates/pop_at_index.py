class StackofPlates:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def getlaststack(self):
        return self.stack[-1]

    def push(self, item):
        if self.stacks == []:
            stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def isEmpty(self):
        last = self.getlaststack()
        return last is None or len(last) == 0

    def popAt(self, index):
        return self.LeftShift(index, true)

    def LeftShift(self, index, removetop):
        stack = self.stacks[index-1]
        #first remove the top of that index stack
        if removetop:
            remove_item = stack[-1]
        #then shift bottom items of next stacks to fill the capacity of the previous stack
        else:
            remove_item = stack.removeBottom()
        if len(stack) == 1:
            del self.stacks[index-1]
        elif len(self.stacks) > index + 2:
            v = self.LeftShift(index + 1, False)
            stack.push(v)

        return remove_item


