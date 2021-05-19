class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        idx = binarysearch(nums, low, high, target)
        # print(idx)
        if idx == -1:
            return (-1, -1)
        i = idx - 1
        j = idx + 1
        # print(i)
        # print(j)
        while i > -1:
            if nums[i] == nums[idx]:
                i = i - 1
            else:
                break
        # print(i)
        while j < len(nums):
            # print(j)
            if nums[j] == nums[idx]:
                j = j + 1
            else:
                break
        return (i + 1, j - 1)


def binarysearch(array, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binarysearch(array, low, mid - 1, target)
        else:
            return binarysearch(array, mid + 1, high, target)
    else:
        return -1