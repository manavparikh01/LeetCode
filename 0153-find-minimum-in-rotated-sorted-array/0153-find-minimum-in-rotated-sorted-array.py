class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        res = nums[l]
        while l <= h:
            if nums[l] <= nums[h]:
                res = min(res, nums[l])
                break
            mid = (l + h) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return res

            