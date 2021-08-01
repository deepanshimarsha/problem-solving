def Grid(m,n, limit):
    if (m,n) == (1,1):
        return 1
    if m < 1:
        return 0
    if n < 1:
        return 0

    elif (m,n) in limit:
        return 0
    
    return Grid(m-1,n,limit) + Grid(m,n-1, limit)

print(Grid(4,4,[(1,2)]))

