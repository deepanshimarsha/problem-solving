class StackofPlates:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, item):
        if self.stacks == []:
            stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if self.stacks == []
            return "stack is empty"
        else:
            poped_item = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                self.stacks[-1].pop()

            return poped_item




