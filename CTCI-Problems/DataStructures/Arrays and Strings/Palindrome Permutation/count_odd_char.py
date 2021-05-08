def PalindromePermutation(str):
    z = ord("z")
    a = ord("a")
    table = [0] * (z-a+1)

    count_odd = 0
    for char in str:
        val = ord(char)
        if val >= a and val <= z:
            idx = val - a
            table[idx] += 1
            if table[idx] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    if count_odd > 1:
        return False
    return True



print(PalindromePermutation("rcaeirca"))