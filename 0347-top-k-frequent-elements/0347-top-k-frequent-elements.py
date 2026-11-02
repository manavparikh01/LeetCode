class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] = hashmap[num] + 1
        heap = []
        for key, values in hashmap.items():
            heapq.heappush(heap, (values, key))
            if len(heap) > k:
                heapq.heappop(heap)
        finallist = []
        for value, key in heap:
            finallist.append(key)
        return finallist