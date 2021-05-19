class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        dict_palin = {}
        for i in range(0, len(s) - 1):
            substring = ""
            j = i
            #print(j)
            #print(len(s))
            while j <= len(s) - 1:
                substring = substring + s[j]
                #print(substring)
                reversed_substring = substring[::-1]
                #print(reversed_substring)
                if substring == reversed_substring:
                    dict_palin[len(substring)] = substring

                j = j + 1

        #print(dict_palin)
        max_length = 0
        for key in dict_palin:
            max_length = max(key, max_length)
        #print(max_length)

        return dict_palin[max_length]

object = Solution()
print(object.longestPalindrome("f"))
word = "word"
print(word[2:len(word):])