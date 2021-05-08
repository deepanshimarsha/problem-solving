#yx will always be a substring of xyxy
#where yx is rotation of xy

def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False

def isSubstring(str1, str2):
    l = len(str2)
    for i in range(len(str1)-l+1):
        if str1[i:i+l] == str2:
            return True
    return False

print(isRotation("waterbottle","erbottlewat"))

