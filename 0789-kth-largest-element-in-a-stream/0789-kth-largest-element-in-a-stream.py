class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.max_heap = nums
        self.k = k
        heapq.heapify(self.max_heap)
        while len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)
            
        return self.max_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)