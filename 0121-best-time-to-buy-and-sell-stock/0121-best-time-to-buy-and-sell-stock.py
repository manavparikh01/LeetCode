class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MIN = prices[0]
        out = 0
        for p in prices:
            #if the p > MIN
            if p > MIN:
                out = max(out, p - MIN)
            #if p <= MIN
            else:
                MIN = p
        return out