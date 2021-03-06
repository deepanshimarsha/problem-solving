class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        curr_max = 0

        while i <= j:
            if height[i] >= height[j]:
                area = (j - i) * height[j]
                j = j - 1
            else:
                area = (j - i) * height[i]
                i = i + 1
            if area >= curr_max:
                curr_max = area
        return curr_max