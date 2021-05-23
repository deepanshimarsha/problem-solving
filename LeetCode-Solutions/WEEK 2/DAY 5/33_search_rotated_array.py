class Solution:
    def search(self, nums, target):
        n = len(nums)
        start, end = 0, n-1

        while start < end:
            mid = (start + end) // 2

            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid+1] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid

        if nums[start] == target:
            return start
        return -1


obj = Solution()
print(obj.search([3,4,5,6,1,2], 2))