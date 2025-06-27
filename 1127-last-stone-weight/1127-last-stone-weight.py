class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return stones[0]
        max_stones = [-stone for stone in stones]
        heapq.heapify(max_stones)
        while len(max_stones) > 1:
            y = -heapq.heappop(max_stones)
            x = -heapq.heappop(max_stones)
            if x == y:
                continue
            else:
                y -= x
                heapq.heappush(max_stones, -y)
        if len(max_stones) == 1:
            return -max_stones[0]
        return 0