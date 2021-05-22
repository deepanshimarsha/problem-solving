class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        while mid > 0 and mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            if nums[mid] > nums[start]:
                mid = mid + 1
            elif nums[mid] < nums[start]:
                mid = mid - 1

        while start <= end:
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                if target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1

            mid = (start + end) // 2

        return -1


obj = Solution()
print(obj.search([3,4,5,6,1,2], 2))