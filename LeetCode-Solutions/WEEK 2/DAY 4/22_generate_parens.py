# category - Recursion
# decision, choices, constraints
class Solution:
    def generateParenthesis(self, n):
        lst = []
        s = ""
        self.backtrack(s, n, n, lst)
        return lst

    def backtrack(self, s, left, right, lst):
        if left < 0 or right < left:
            return
        if left == 0 and right == 0:
            lst.append(s)
            return
        else:
            if left > 0:
                self.backtrack(s+"(", left-1, right, lst)
            if right > left:
                self.backtrack(s+")", left, right-1, lst)

obj = Solution()
print(obj.generateParenthesis(3))


