#time complexity - O(n^2)
#space complexity - O(n)

#if we are allowed to use unlimited stacks
# we could implement merge sort or quick sort recursively

def SortStack(stack):
    temp_stack = []
    while len(stack) != 0:
        temp = stack.pop()
        while len(temp_stack) != 0 and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)

    return temp_stack

print(SortStack([5,10,7,3,12,8,1]))
