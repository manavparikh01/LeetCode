class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dp(i, sum):
            if i >= len(candidates) or sum > target:
                return
            if sum == target:
                res.append(temp.copy())
                return
            sum += candidates[i]
            temp.append(candidates[i])
            dp(i, sum)
            sum -= candidates[i]
            temp.pop()
            dp(i+1, sum)
        dp(0, 0)
        return res
        