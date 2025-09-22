class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefixsum = [0] * len(s)
        prefixltor = [-1] * len(s)
        prefixrtol = [-1] * len(s)
        prefixsum[0] = 0 if s[0] == '|' else 1
        for ind, cha in enumerate(s):
            if ind > 0:
                prefixltor[ind] = prefixltor[ind - 1]
                prefixsum[ind] = prefixsum[ind - 1]
            if cha == '|':
                prefixltor[ind] = ind
            else:
                if ind > 0:
                    prefixsum[ind] = prefixsum[ind] + 1
        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1:
                prefixrtol[i] = prefixrtol[i + 1]
            if s[i] == '|':
                prefixrtol[i] = i
        # print(prefixsum)
        # print(prefixltor)
        # print(prefixrtol)
        res = []
        for query in queries:
            count = 0
            if query[0] < query[1]:
                candleleft = prefixrtol[query[0]]
                candleright = prefixltor[query[1]]
                count = prefixsum[candleright] - prefixsum[candleleft] if candleleft < candleright else 0
            res.append(count)
        return res