class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = []
        count = 0
        curr_count = 0
        repeat = 0
        if len(s) == 1:
            return 1
        if s == " ":
            return 1

        for i in range(0, len(s)):

            i = repeat

            while s[i] not in seen:
                seen.append(s[i])
                i = i + 1
                if i >= len(s):
                    break

            # print(seen)

            repeat = i
            # print(repeat)
            count = max(count, len(seen))
            if repeat >= len(s):
                break
            index1 = seen.index(s[repeat])
            # print(index1)
            for j in range(0, index1 + 1):
                seen.pop(0)

        return count


object = Solution()
object.lengthOfLongestSubstring("au")