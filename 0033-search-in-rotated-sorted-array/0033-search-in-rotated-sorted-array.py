class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if nums[mid] > target or target > nums[h]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1