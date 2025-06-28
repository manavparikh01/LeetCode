class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > len(nums)-k+1:
                heapq.heappop(max_heap)
        return -max_heap[0]