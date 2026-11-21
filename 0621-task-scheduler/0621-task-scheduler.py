class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1
        maxheap = []
        for values in hashmap.values():
            heapq.heappush(maxheap, -values)
        queue = deque()
        time = 0
        while maxheap or queue:
            time += 1
            if maxheap:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] <= time:
                heapq.heappush(maxheap, queue.popleft()[0])
        return time