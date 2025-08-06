class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = defaultdict(list)
        for p, q, r in times:
            hashmap[p].append((q, r))
        min_heap = [(0, k)]
        visit = set()
        time = 0
        while min_heap:
            w1, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, w1)
            for node2, w2 in hashmap[node]:
                if node2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, node2))
        return time if len(visit) == n else -1 
                    