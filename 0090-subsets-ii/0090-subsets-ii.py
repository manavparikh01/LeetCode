class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        def dp(i):
            nonlocal res, temp
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            dp(i + 1)
            temp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dp(i + 1)
            return
        dp(0)
        return res