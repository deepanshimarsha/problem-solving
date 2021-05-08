def CheckPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    count = [0] * 256

    for i in range(len(str1)):
        count[ord(str1[i])] += 1
    for j in range(len(str2)):
        count[ord(str2[j])] -= 1

    for i in range(256):
        if count[i] != 0:
            return False
    return True

print(CheckPermutation("dog","gtd"))