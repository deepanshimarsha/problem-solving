def TripleStep(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return TripleStep(n-1) + TripleStep(n-2) + TripleStep(n-3)

print(TripleStep(4))