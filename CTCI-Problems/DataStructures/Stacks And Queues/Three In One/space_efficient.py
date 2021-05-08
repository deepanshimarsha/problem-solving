class kstacks:
    def __init__(self,k,n):
        self.k = k  #no of stacks
        self.n = n  #total size of array
        self.arr = [0] * self.n
        self.top = [-1]*self.k  #hold top indexes of k stack
        self.free = 0  #holds index of free space in array
        self.next = [i+1 for i in range(self.n)]  #points to the next element in one of the k stack or the free stack
        self.next[self.n - 1] = -1

    def isEmpty(self, stacknum):
        return self.top[stacknum] == -1

    def isFull(self):
        return self.free == -1

    def push(self, item, stacknum):
        if self.isFull():
            print("stack overflow")
            return

        #get the free position
        insert_at = self.free

        #set the free position
        self.free = self.next[insert_at]

        #insert element
        self.arr[insert_at] = item

        #update next to point at previous element in kth stack
        self.next[insert_at] = self.top[stacknum]

        #update the top of kth stack
        self.top[stacknum] = insert_at

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return
        #get top of the stack
        top_of_stack = self.top[stacknum]

        #update top of the stack
        self.top[stacknum] = self.next[top_of_stack]

        #update next to point to previous of the top
        self.next[top_of_stack] = self.free

        #update free to the popped index
        self.free = top_of_stack

        self.arr.pop(top_of_stack)

    def printstack(self, stacknum):
        top_of_stack = self.top[stacknum]
        while top_of_stack != -1:
            print(self.arr[top_of_stack])
            top_of_stack = self.next[top_of_stack]


if __name__ == "__main__":
    # Create 3 stacks using an
    # array of size 12.
    obj = kstacks(3, 12)

    # Push some items onto stack number 2.
    obj.push(15, 2)
    obj.push(45, 2)
    #obj.printstack(2)

    # Push some items onto stack number 1.
    obj.push(17, 1)
    obj.push(49, 1)
    obj.printstack(1)
    obj.pop(1)
    obj.printstack(1)




