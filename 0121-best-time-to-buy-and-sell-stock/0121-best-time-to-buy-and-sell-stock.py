class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower_num = prices[0]
        sum_out = 0
        for i in prices:
            if i < lower_num:
                lower_num = i
            else:
                sum_out = max(sum_out, i - lower_num)
        return sum_out