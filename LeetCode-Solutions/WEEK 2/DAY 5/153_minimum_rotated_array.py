class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return min(nums)
        i = 0
        j = len(nums)-1
        if nums[i] < nums[j]:
            return nums[i]
        while i < j:
            if nums[i] < nums[i+1]:
                i = i + 1
            else:
                return nums[i+1]
            if nums[j] > nums[j-1]:
                j = j -1
            else:
                return nums[j]