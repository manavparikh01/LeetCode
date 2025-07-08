class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()
        def dp(i, sum):
            if sum == target:
                if temp in res:
                    return
                res.append(temp.copy())
                return
            if i >= len(candidates) or sum > target:
                return
            sum += candidates[i]
            temp.append(candidates[i])
            dp(i + 1, sum)
            sum -= candidates[i]
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dp(i + 1, sum)
        dp(0, 0)
        return res