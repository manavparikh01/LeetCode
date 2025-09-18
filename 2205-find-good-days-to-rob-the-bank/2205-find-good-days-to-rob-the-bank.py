class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        ltor = [0] * len(security)
        rtol = [0] * len(security)
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                ltor[i] = ltor[i - 1] + 1
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                rtol[i] = rtol[i + 1] + 1
        res = []
        for i in range(len(security)):
            if ltor[i] >= time and rtol[i] >= time:
                res.append(i)
        return res