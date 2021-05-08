#time complexity - O(nlogn)
def UniqueCharacters(str):
    str = sorted(str)
    for i in range(0, len(str)-1):
        if str[i] == str[i+1]:
            return False
    return True

