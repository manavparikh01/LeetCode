class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        minheap = []
        for boxes in boxTypes:
            heapq.heappush(minheap, [-boxes[1], boxes[0]])
        res = 0
        while truckSize > 0 and minheap: 
            units, boxes = heapq.heappop(minheap)
            val = -units
            minbox = min(boxes, truckSize)
            res += val * minbox
            truckSize -= minbox
        return res