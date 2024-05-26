class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        man = 0
        maxi = 0
        for i in range(1, len(prices), 1):
            if prices[i] < prices[man]:
                man = i
            else:
                maxi = max(maxi, prices[i] - prices[man])
        return maxi