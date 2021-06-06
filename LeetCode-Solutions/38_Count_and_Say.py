class Solution:
    def countAndSay(self, n: int) -> str:
        s = ""
        return recursion(1, n, s)
    
def recursion(digit,n,s):
    if digit > n:
        return s
    
    if digit == 1:
        s += "1"
        return recursion(digit+1, n, s)
        
    else:
        #say s
        j = 0
        for i in range(0, len(s)):
            i = j
            c = 1
            if i > len(s) - 1:
                break
            if i == len(s) - 1:
                s = s[0:j] + "1" + s[j]
                break
            while i < len(s)-1 and s[i] == s[i+1]:
                i += 1
                c += 1
            s = s[0:j] + str(c) + s[j] + s[i+1:]
            j = i + 1
        return recursion(digit+1, n, s)

obj = Solution()
print(obj.countAndSay(4))