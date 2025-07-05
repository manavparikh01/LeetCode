class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i):
            nonlocal res
            nonlocal temp
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()
            backtrack(i + 1)
            

        backtrack(0)
        return res
        