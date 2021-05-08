#time complexity - O(nlogn)

def CheckPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    str1 = "".join(str1)
    str2 = "".join(str2)
    #print(str1,str2)

    return str1 == str2

print(CheckPermutation("god","dog"))