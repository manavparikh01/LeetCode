class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = 0
        for i in range(len(intervals)):
            # print(intervals[i], newInterval)
            curr = i
            if intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                continue
            if intervals[i][0] > newInterval[0] and intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = [-1,-1]
                res.append(intervals[i])
                break
            if intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1]:
                res.append(intervals[i])
                newInterval = [-1,-1]
                break
            if intervals[i][0] >= newInterval[0] and intervals[i][1] >= newInterval[1]:
                # print(intervals[i], newInterval)
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                res.append(newInterval)
                newInterval = [-1,-1]
                break
            if (intervals[i][0] >= newInterval[0] or intervals[i][0] <= newInterval[0]) and intervals[i][1] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                continue
        if newInterval != [-1,-1]:
            res.append(newInterval)
        if curr == len(intervals) - 1:
            return res
        for j in range(curr + 1, len(intervals)):
            if intervals[j] not in res:
                res.append(intervals[j])
        return res
            