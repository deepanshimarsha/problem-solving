#time complexity - O(n)
#using extra sppace
#idea is to maintain a boolean array for the characters

def UniqueCharacters(str):
    #assume we have extended ASCII(8 bits)
    max_char = 256

    if len(str) > 256:
        return False

    bool_array = [False] * max_char
    for i in range(len(str)-1):

        #int value of character
        idx = ord(str[i])

        if (bool_array[idx] == True):
            return False
        bool_array[idx] = True

    return False