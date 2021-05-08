def hourglasssum(arr):
    lists = []

    for i in range(0, 4):
        for j in range(0, 4):
            lists.append(sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]) )



    print(max(lists))
    print(1^7)

hourglasssum([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 7, 8, 9], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])