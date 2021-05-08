stack1, stack2 = [], []
for _ in range(int(input())):
    f = list(map(int, input().split()))
    if f[0] == 1:
        stack1.append(f[1])
    elif f[0] == 2:
        if len(stack2) == 0:
            while stack1:
                stack2.append(stack1.pop())
        stack2.pop()
    else:
        if len(stack2) != 0:
            print(stack2[-1])
        else:
            print(stack1[0])





