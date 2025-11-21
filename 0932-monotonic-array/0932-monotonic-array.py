class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        diff = nums[-1] - nums[0]
        if diff > 0:
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] < 0:
                    return False
        elif diff < 0:
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] > 0:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] != 0:
                    return False
        return True