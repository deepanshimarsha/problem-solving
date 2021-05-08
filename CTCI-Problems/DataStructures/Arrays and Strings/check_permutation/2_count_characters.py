#assumptions -
#string is ASCII 8 bits - 256 character range
#character is both string is small

def CheckPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    count1 = [0]*256
    count2 = [0]*256

    for i in range(len(str1)):
        count1[ord(str1[i])] += 1

    for j in range(len(str2)):
        count2[ord(str2[j])] += 1

    #compare count array
    for i in range(0, 256):
        if count1[i] != count2[i]:
            return False
    return True

print(CheckPermutation("god","dtg"))