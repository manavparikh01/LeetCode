class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        for word in words:
            hashmap[word] += 1
        minheap = []
        for word, freq in hashmap.items():
            heapq.heappush(minheap, [-freq, word])
            # if len(minheap) > k:
            #     heapq.heappop(minheap)
        res = []
        while k > 0:
            res.append(heapq.heappop(minheap)[1])
            k -= 1
        return res