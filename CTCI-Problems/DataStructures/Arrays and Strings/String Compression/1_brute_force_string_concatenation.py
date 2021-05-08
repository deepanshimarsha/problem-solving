#time complexity - O(p + k**2)
#its slow
#string concatenation operates in O(n**2)

def StringCompression(str1):
    count = 0
    compressed_str = ""
    for i in range(0, len(str1)):
        count += 1
        if (i+1 >= len(str1)) or str1[i] != str1[i+1]:
            compressed_str += "" + str(str1[i]) + str(count)
            count = 0
    if len(compressed_str) < len(str1):
        return compressed_str
    return str1

print(StringCompression("aabcccccaaa"))
