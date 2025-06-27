class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []
        hash_map = {}
        res = []
        for point in points:
            temp_val = point[0]**2 + point[1]**2
            heapq.heappush(min_heap, -temp_val)
            if temp_val not in hash_map:
                hash_map[temp_val] = [point]
            else:
                hash_map[temp_val].append(point)
            if len(min_heap) > k:
                pop_val = -heapq.heappop(min_heap)
                del hash_map[pop_val][0]
        for point in hash_map.values():
            for arr in point:
                res.append(arr)
        return res