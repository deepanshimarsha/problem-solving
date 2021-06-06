class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        j = 0
        i = 0
        if len(strs) == 0:
            return res

        if len(strs) == 1:
            if len(strs[i]) == 0:
                return res
            else:
                return strs[i]

        while len(strs[i]) > 0 and len(strs[i + 1]) > 0 and strs[i][j] == strs[i + 1][j]:
            i = i + 1
            if i == len(strs) - 1:
                res = res + strs[i][j]
                i = 0
                j = j + 1
            if j > len(strs[i]) - 1 or j > len(strs[i + 1]) - 1:
                break
        return res
