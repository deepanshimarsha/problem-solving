def largestRectangle(h):
    max_area = h[0]
    l = len(h)
    for i in range(l):
        count = 0
        j = i
        k = i - 1
        if h[i] <= h[j]:
            while j < l and h[i] <= h[j]:
                count += 1
                j += 1

        if h[i] <= h[k]:
            while k >= 0 and h[i] <= h[k]:
                count += 1
                k -= 1

        area = count * h[i]
        max_area = max(area, max_area)
    return max_area

print(largestRectangle([6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494]))