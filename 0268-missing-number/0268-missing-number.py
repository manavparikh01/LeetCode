class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res = res ^ i
        for i in nums:
            res = res ^ i
        return res
