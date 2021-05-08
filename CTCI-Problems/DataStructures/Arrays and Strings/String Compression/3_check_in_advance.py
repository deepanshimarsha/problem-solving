def StringCompression(str1):
    final_length = CompressedLength(str1)
    if final_length >= len(str1):
        return str1
    return CompressedStr(str1)

def CompressedStr(str1):
    count = 0
    compressed_lst = []
    for i in range(len(str1)):
        count += 1
        if i + 1 >= len(str1) or str1[i] != str1[i + 1]:
            compressed_lst.append(str(str1[i]))
            compressed_lst.append(str(count))
            count = 0

    return "".join(compressed_lst)

def CompressedLength(str1):
    compressed_len = 0
    count = 0
    for i in range(len(str1)):
        count += 1
        if i+1 >= len(str1) or str1[i] != str1[i+1]:
            compressed_len += 1 + len(str(count))
            count = 0
    return compressed_len

print(StringCompression("abc"))
