class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        max_heap = []
        for task in tasks:
            freq[task] = 1 + max(freq.get(task), 0)
        for value in freq.values():
            heapq.heappush(max_heap, -value)
        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                count = 1+ heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                val = queue.popleft()[0]
                heapq.heappush(max_heap, val)

        return time