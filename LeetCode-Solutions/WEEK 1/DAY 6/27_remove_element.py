class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        k = len(nums)
        j = 0
        for i in range(0, k):
            i = j
            # print(i)
            if i >= len(nums):
                break
            if nums[i] == val:
                nums.pop(i)
                j = i
            else:
                count = count + 1
                j = i + 1
        return count
