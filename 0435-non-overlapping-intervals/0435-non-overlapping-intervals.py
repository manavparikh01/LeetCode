class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        preend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= preend:
                preend = end
            else:
                res += 1
                preend = min(preend, end)
        return res