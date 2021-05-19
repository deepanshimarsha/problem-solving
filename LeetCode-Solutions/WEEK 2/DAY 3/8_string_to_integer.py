#category - DS, String
#logic - ASCII code
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = []
        for i in s:
            if i in ["-", "+"] and len(res) == 0:
                res.append(i)
            elif ord(i) in range(48, 58):
                res.append(i)
            else:
                break

        if len(res) == 0 or (len(res) == 1 and res[0] in ["-","+"]):
            return 0

        digit = int("".join(res))
        if digit > 2**31-1:
            return 2**31-1
        elif digit < -2**31:
            return -2**31
        else:
            return digit

object = Solution()
print(object.myAtoi("987"))

