class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = max(nums).bit_length()
        mask = 1 << k
        dp = [0] * mask
        for a in nums:
            dp[a] = a
        for i in range(mask):
            if dp[i]: continue
            for j in range(k):
                if i & (1 << j):
                    if dp[i ^ (1 << j)] > dp[i]:
                        dp[i] = dp[i ^ (1 << j)]
        return max(a * dp[(mask - 1) ^ a] for a in nums)