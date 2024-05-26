class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = nums[0]
        max1 = nums[0]
        for i in range(1, len(nums), 1):
            sum1 = max(sum1+nums[i], nums[i])
            max1 = max(max1, sum1)
            print("sum", sum1)
        return max1