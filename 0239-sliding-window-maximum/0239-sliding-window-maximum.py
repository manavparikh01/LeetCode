class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxheap = []
        for i in range(k):
            heapq.heappush(maxheap, (-nums[i], i))
        res.append(-maxheap[0][0])
        if len(nums) > k:
            for i in range(k, len(nums)):
                heapq.heappush(maxheap, (-nums[i], i))
                while maxheap[0][1] < i - k + 1:
                    heapq.heappop(maxheap)
                res.append(-maxheap[0][0])
        return res
