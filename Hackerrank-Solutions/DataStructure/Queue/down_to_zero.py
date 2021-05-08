def multiples(N):
    mult_min = 1000000
    for a in range(2, N):
        if N % a == 0:
            #print(a)
            b = N//a
            #print(N)
            #print(a, b)
            print(max(a, b))
            mult_min = min(max(a,b), mult_min)
        else:
            continue
    return mult_min

def down2zero(N):
    count = 0
    while N != 0:
        query1 = N-1
        query2 = multiples(N)
        print(query1, query2)
        if query1 <= query2:
            N = query1
        else:
            N = query2
        count += 1
    print(count)



#down2zero(812849)
multiples(812848)