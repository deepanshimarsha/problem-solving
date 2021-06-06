class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        pair = ['()', '{}', '[]']
        stack = []
        for i in range(0, len(s)):
            # print(i)
            if s[i] in opening:
                stack.append(s[i])
                # print(stack)
            else:
                if len(stack) != 0 and stack[-1] + s[i] in pair:
                    stack.pop(-1)

                elif len(stack) == 0 or (stack[-1] + s[i]) not in pair:
                    # print(stack[-1]+s[i])
                    return False
                else:
                    return True
        if len(stack) == 0:
            return True
        else:
            return False
