class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return -1
        max_heap = []  
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > len(nums) - k + 1:
                heapq.heappop(max_heap)
            # print(max_heap)
        return -max_heap[0]
