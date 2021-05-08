def createseq(n, queries, q):
    lastanswer = 0
    seqList = [[] for i in range(n)]

    lists = []
    for i in range(q):
        Q = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]

        if Q == 1:
            index = (x ^ lastanswer) % n
            seqList[index].append(y)
            print(seqList)
            print(index)

        else:
            index = (x ^ lastanswer) % n
            print(index)
            size = y % len(seqList[index])
            lastanswer = seqList[index][size]
            lists.append(lastanswer)

    return lists


print(createseq(2, [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]], 5))










