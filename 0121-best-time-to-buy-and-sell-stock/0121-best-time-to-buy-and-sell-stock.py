class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = len(prices) - 1
        min = len(prices) - 1
        diff = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[maxi] - prices[i] == 0:
                continue
            elif prices[maxi] - prices[i] < 0:
                maxi = i
            else:
                diff = max(prices[maxi] - prices[i], diff)
        return diff