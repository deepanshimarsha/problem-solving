def DenseArray(a):
    count = 0
    for i in range(0, len(a)-1):
        #print(i)
        max_num = max(a[i], a[i+1])
        min_num = min(a[i], a[i+1])
        if (max(a[i], a[i+1]) / min(a[i], a[i+1])) > 2:
            num = min_num*2
            while num < max_num:
                num = num*2
                count = count + 1

    return count

print(DenseArray([42, 16]))

