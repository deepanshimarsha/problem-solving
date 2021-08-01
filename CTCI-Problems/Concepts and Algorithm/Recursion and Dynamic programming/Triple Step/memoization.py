def TripleStep(n, memo):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = TripleStep(n-1, memo) + TripleStep(n-2, memo) + TripleStep(n-3, memo)
        return memo[n]


n = 3
memo = {}
for i in range(1,n+1):
    memo[i] = -1
print(TripleStep(n, memo))