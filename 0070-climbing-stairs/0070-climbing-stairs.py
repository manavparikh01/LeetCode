class Solution:
    def climbStairs(self, n: int) -> int:
        lists = [0] * (n+1)
        lists[n] = 1
        lists[n-1] = 1
        for i in range(n-2, -1, -1):
            lists[i] = lists[i+1] + lists[i+2]
        return lists[0]