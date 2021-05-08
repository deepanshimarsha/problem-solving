def waiter(number, q):
    A_before = number
    A = []
    B = []
    lower = 2
    upper = 10000
    prime = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]
    
    for i in range(q):
        while len(A_before) != 0:
            poped_item = A_before.pop()
            if poped_item % prime[i] == 0:
                B.append(poped_item)
            else:
                A.append(poped_item)
        # print(B)
        while len(B) != 0:
            print(B.pop())
        # print(A)
        if i != q - 1:
            while len(A) != 0:
                A_before.append(A.pop())
        else:
            while len(A) != 0:
                print(A.pop())


if __name__ == '__main__':
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    waiter(number, q)
