class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_value = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] < max_value:
                profit = max_value - prices[i]
                max_profit = max(max_profit, profit)
            else:
                max_value = prices[i]
        return max_profit