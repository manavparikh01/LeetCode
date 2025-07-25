class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        for i in range(2, len(nums)):
            maxval = 0
            for j in range(0, i-1):
                maxval = max(maxval, arr[j])
            arr[i] = nums[i] + maxval
        
        return max(arr[-1], arr[-2])