t = int(input())
lists = []
for i in range(t):
    x = list(map(int, input().split()))
    lists.append(x)


def ThreeSwimmers(time):
    p = time[0]
    time.sort()
    i = time.index(p)
    if i == len(time)-1:
        k = 2
        for j in range(0,len(time)-1):
            #print(p)
            #print(k * time[j])
            while p > (k * time[j]):
                #print(j)
                j = j + 1
                if j == len(time)-1:
                    j = 0
                    k = k + 1
            #print(k*time[j])
            return (k*time[j] - p)




    return time[i+1]-p

answer = [ThreeSwimmers(x) for x in lists]
for ans in answer:
    print(ans)

#print(ThreeSwimmers([10, 9, 9, 9]))