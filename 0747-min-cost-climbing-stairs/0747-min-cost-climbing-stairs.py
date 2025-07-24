class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        arr = [0] * len(cost)
        arr[len(cost)-1] = cost[-1]
        arr[len(cost)-2] = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            arr[i] = min(arr[i+1]+cost[i], arr[i+2]+cost[i])
        return min(arr[0], arr[1])