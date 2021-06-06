class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sums = 0
        j = 0
        for k in range(0, len(s)):
            k = j
            if k > len(s) - 1:
                break
            if k <= len(s) - 2 and roman_int[s[k]] < roman_int[s[k + 1]]:
                sums = sums + roman_int[s[k + 1]] - roman_int[s[k]]
                j = k + 2
            else:
                sums = sums + roman_int[s[k]]
                j = k + 1
        return sums
