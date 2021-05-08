def OneAway(str1, str2):
    if len(str1) == len(str2):
        return Replacement(str1, str2)
    elif len(str1) + 1 == len(str2):
        return InsertionRemoval(str1, str2)
    else:
        return InsertionRemoval(str2, str1)

    return False

def Replacement(str1, str2):
    #all characters identical except one
    found_diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            found_diff += 1
            if found_diff > 1:
                return False
    if found_diff == 0:
        return False
    return True

def InsertionRemoval(str1, str2):
    #all characters identical by a shift
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        #print(i, j)
        if str1[i] != str2[j]:
            #print(i, j)
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1

    return True


print(OneAway("aple", "apple"))