class MedianFinder(object):

    def __init__(self):
        self.leftheap = []
        self.rightheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.leftheap) == 0 or len(self.rightheap) == 0:
            heapq.heappush(self.leftheap, -num)
        # elif len(self.rightheap) == 0:
        #     heapq.heappush(self.rightheap, num)
        else:
            if num <= -self.leftheap[0]:
                heapq.heappush(self.leftheap, -num)
            else:
                heapq.heappush(self.rightheap, num)
        if len(self.leftheap) - len(self.rightheap) == 2:
                temp = -heapq.heappop(self.leftheap)
                heapq.heappush(self.rightheap, temp)
        if len(self.rightheap) - len(self.leftheap) == 2:
                temp = heapq.heappop(self.rightheap)
                heapq.heappush(self.leftheap, -temp)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.leftheap) == len(self.rightheap):
            return (float)(-self.leftheap[0] + self.rightheap[0])/2
        elif len(self.leftheap) > len(self.rightheap):
            return -self.leftheap[0]
        else:
            return self.rightheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()