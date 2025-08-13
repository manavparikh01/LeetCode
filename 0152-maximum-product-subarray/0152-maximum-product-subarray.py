class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minpro, maxpro = 1, 1
        for i in nums:
            if i == 0:
                minpro, maxpro = 1, 1
            tempro = maxpro * i
            maxpro = max(maxpro * i, minpro * i, i)
            minpro = min(tempro, minpro * i, i)
            res = max(res, maxpro)
        return res