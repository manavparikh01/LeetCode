class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        i = 0
        while i < len(nums):
            mintotal = 0
            while i < len(nums) and nums[i] == 1:
                i += 1
                mintotal += 1
            i += 1
            total = max(total, mintotal)
        return total
            
                