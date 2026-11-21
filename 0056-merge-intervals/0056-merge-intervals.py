class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        heap = []
        for interval in intervals:
            heapq.heappush(heap, interval)
        res = [heapq.heappop(heap)]
        while heap:
            interval = heapq.heappop(heap)
            if len(res) > 0 and interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res