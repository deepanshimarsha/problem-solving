#category - Algorithm
def maxProduct(nums):
    res = max(nums)
    currMin = 1
    currMax = 1

    for n in nums:
        if n == 0:
            currMax = 1
            currMin = 1
            continue
        tmp = currMax * n
        #print(tmp)
        currMax = max(tmp, n * currMin, n)
        currMin = min(n * currMin, tmp, n)
        res = max(res, currMax)
    return res


print(maxProduct([0]))
