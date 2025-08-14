class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        overSum = 0
        first = 0
        for i in range(len(gas)):
            sumrn = gas[i] - cost[i]
            overSum += sumrn
            if overSum < 0:
                overSum = 0
                first = i + 1
        return first