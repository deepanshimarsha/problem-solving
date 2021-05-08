#time complexity - O(p+k)

def StringCompression(str1):
    count = 0
    compressed_lst = []
    for i in range(len(str1)):
        count += 1
        if i+1 >= len(str1) or str1[i] != str1[i+1]:
            compressed_lst.append(str(str1[i]))
            compressed_lst.append(str(count))
            count = 0

    compressed_str = "".join(compressed_lst)
    if len(compressed_str) < len(str1):
        return compressed_str
    return str1

print(StringCompression("aabcccccaaa"))
