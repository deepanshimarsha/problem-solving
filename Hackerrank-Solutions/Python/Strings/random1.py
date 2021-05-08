def consecutive(array):
    j = 0
    k = 0
    for i in range(len(array)):
        i = j
        if i <=
            k = i
            j = i + 1
            while array[j] == array[k] + 1:
                k = j
                j = k + 1
            if k == i + 1:
                print(array[i], end=",")
            else:
                print(array[i],end="-")

        else:
            print(array[i])

consecutive([1,2,4,6,7,8,9,10])