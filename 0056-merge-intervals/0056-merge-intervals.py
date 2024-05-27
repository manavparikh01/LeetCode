class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals)
        def sort_by_first(sublist):
            return sublist[0]

        pintervals = sorted(intervals, key=sort_by_first)
        ans = []
        i = 0
        while i < l-1:
            pre = []
            pre.append(pintervals[i][0])
            pre.append(pintervals[i][1])
            while i < l-1 and pre[1] >= pintervals[i+1][0]:
                pre[1] = max(pintervals[i+1][1], pre[1])
                i += 1
            ans.append(pre)
            i += 1
        if i == l - 1:
            ans.append(pintervals[i])
        return ans