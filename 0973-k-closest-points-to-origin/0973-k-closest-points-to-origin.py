class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minheap = []
        res = []
        for point in points:
            dis = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(minheap, (-dis, point))
            if len(minheap) > k:
                heapq.heappop(minheap)
        while minheap:
            heap = heapq.heappop(minheap)
            res.append(heap[1])
        return res