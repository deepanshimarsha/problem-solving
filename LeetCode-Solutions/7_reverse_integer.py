class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = abs(x)
            rev = -ReverseInt(x)
        else:
            rev = ReverseInt(x)
        if rev in range(-2147483648, 2147483648):
            return rev
        else:
            print(rev)
            return 0


def ReverseInt(n):
    rev = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev
