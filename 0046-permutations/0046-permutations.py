class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dp():
            nonlocal res, temp
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for ind in range(0, len(nums)):
                if nums[ind] not in temp:
                    temp.append(nums[ind])
                    dp()
                    temp.pop()
            return
        dp()
        return res