def MexMax(s,k):
    l = len(s)
    s = sorted(s)
    for i in range(0,k):

        Max = max(s)
        if s[0] == 0:
            j = 0
            while j < len(s)-1 and (s[j+1] == s[j] + 1 or s[j+1] == s[j]):
                j = j + 1
            Mex = s[j] + 1
        else:
            Mex = 0

        num = (Max + Mex) // 2
        if num in s:
            s.append(num)

    seen = set()
    for i in range(0,l):
        if s[i] not in seen:
            seen.add(s[i])
    return len(seen)

print(MexMax([0,1,3,4], 2))

