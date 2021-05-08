def twoStacks(x, a, b):
    total = 0
    atmp = []
    for i in range(0, len(a)):
        val = a.pop()
        if total + val > x:
            break
        total += val
        atmp.append(val)
    max_count = len(atmp)
    curr_count = max_count
    while len(b):
        if total + b[-1] <= x:
            total += b.pop()
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        total -= aval
        curr_count -= 1

    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n, m, x = input().strip().split(' ')
        n, m, x = [int(n), int(m), int(x)]

        a = list(map(int, reversed(input().strip().split(' '))))

        b = list(map(int, reversed(input().rstrip().split(' '))))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()