class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i == 0:
                continue
            res.add(i)
        return len(res)