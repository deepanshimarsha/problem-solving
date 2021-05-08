def equalStacks(h1, h2, h3):
    h1_height = sum(h1)
    h2_height = sum(h2)
    h3_height = sum(h3)

    min_height = min(h1_height, h2_height, h3_height)
    for i in range(0, min_height):
        if h1_height > min_height:
            while h1_height > min_height:
                poped_item = h1.pop(0)
                h1_height -= poped_item
        if h2_height > min_height:
            while h2_height > min_height:
                poped_item = h2.pop(0)
                h2_height -= poped_item
        if h3_height > min_height:
            while h3_height > min_height:
                poped_item = h3.pop(0)
                h3_height -= poped_item
        if h1_height == h2_height and h2_height == h3_height:
            return h1_height
        else:
            min_height = min(h1_height, h2_height, h3_height)

print(equalStacks([3,2,1,1,1],[4,3,2],[1,1,4,1]))