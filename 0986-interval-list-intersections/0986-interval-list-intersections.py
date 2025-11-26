class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        l1, l2 = len(firstList), len(secondList)
        res = []
        m, n = 0, 0
        while m < l1 and n < l2:
            l11, l12 = firstList[m][0], firstList[m][1]
            l21, l22 = secondList[n][0], secondList[n][1]
            # print(l11, l12, l21, l22)
            if l12 < l21:
                m += 1
            elif l22 < l11:
                n += 1
            else:
                i, j = max(l11, l21), min(l12, l22)
                res.append([i, j])
                if l12 < l22:
                    m += 1
                elif l12 > l22:
                    n += 1
                else:
                    m += 1
                    n += 1
        return res