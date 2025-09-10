class Solution:
    def reorganizeString(self, s: str) -> str:
        priorityh = []
        sph = []
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] = hashmap[char] + 1
        for key, val in hashmap.items():
            heapq.heappush(priorityh, [-val, key])
        res = ""
        while priorityh:
            freq, key = heapq.heappop(priorityh)
            res += key
            if sph:
                f, k = heapq.heappop(sph)
                heapq.heappush(priorityh, [f, k])
            if freq < -1:
                heapq.heappush(sph, [freq + 1, key])
        while sph:
            freq, key = heapq.heappop(sph)
            if res[-1] == key:
                return ""
            if freq < -1:
                return ""
            res += key
        return res