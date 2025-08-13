class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        l = 0
        sumtn = nums[l]
        for i in range(1, len(nums)):
            sumtn = max(nums[i], nums[i] + sumtn)
            maxsum = max(maxsum, sumtn)
        return maxsum