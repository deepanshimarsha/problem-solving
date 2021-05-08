#category - Algorithm
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for i in range(len(nums)):
            j = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while i < j - 2:
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j = j - 1
                    continue
                l = i + 1
                r = j - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r] + nums[j]
                    if total < target:
                        l = l + 1
                    elif total > target:
                        r = r - 1
                    else:
                        res.append([nums[i], nums[l], nums[r], nums[j]])

                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l = l + 1
                        r = r - 1
                j = j - 1
        return res