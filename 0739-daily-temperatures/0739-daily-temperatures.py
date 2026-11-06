class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        monotonicstack = []
        restemp = [0] * len(temperatures)
        print(len(restemp))
        for i in range(len(temperatures) - 1, -1, -1):
            while len(monotonicstack) > 0 and monotonicstack[-1][0] <= temperatures[i]:
                monotonicstack.pop()
            # print(temperatures[i], i, monotonicstack)
            if len(monotonicstack) == 0:
                restemp[i] = 0
            else:
                restemp[i] = monotonicstack[-1][1] - i
            monotonicstack.append([temperatures[i], i])
        return restemp