class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum = 0
        i = 0
        for num in nums:
            sum += num
        target = sum - x
        res = 0
        maxval = -1
        for j in range(len(nums)):
            res += nums[j]

            while i <= j and res > target:
                res -= nums[i]
                i += 1
            
            if res == target:
                maxval = max(maxval, j - i + 1)
        
        return -1 if maxval == -1 else len(nums) - maxval
    