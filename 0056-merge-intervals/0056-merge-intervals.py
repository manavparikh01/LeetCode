class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x:x[0])
        i = 0
        res = []
        while i < len(sortedIntervals) - 1:
            curr = i
            secondpart = sortedIntervals[curr][1]
            while i < len(sortedIntervals) - 1 and sortedIntervals[i+1][0] <= secondpart:
                i += 1
                secondpart = max(secondpart, sortedIntervals[i][1])
            res.append([sortedIntervals[curr][0], secondpart])
            i += 1
        print(i)
        if i == len(sortedIntervals) - 1:
            res.append(sortedIntervals[i])
        return res