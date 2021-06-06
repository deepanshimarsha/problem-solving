class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        count = 0
        for i in range(0, len(nums)):
            i = j
            count = count + 1
            # print(len(nums))
            # print(i)
            if i >= len(nums) - 1:
                break
            while nums[i] == nums[i + 1]:
                poped_item = nums.pop(i + 1)
                if i >= len(nums) - 1:
                    break
                # print(poped_item)

            j = i + 1
            # print(j)
        return count
