class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        poslen = 0
        neglen = 0
        res = 0
        for num in nums:
            if num > 0:
                poslen += 1
                if neglen != 0:
                    neglen += 1
            elif num < 0:
                temp = poslen
                if neglen == 0:
                    poslen = 0
                else:
                    poslen = neglen + 1
                neglen = temp + 1
            else:
                poslen = 0
                neglen = 0
            res = max(res, poslen)
        return res