class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in nums:
            dpn = defaultdict(int)
            for curr_sum, count in dp.items():
                dpn[curr_sum + i] += count
                dpn[curr_sum - i] += count
            dp = dpn
        
        return dp[target]