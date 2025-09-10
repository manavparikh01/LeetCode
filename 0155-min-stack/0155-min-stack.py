class MinStack:

    def __init__(self):
        self.list = []
        self.heap = []


    def push(self, val: int) -> None:
        self.list.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        lastindex = len(self.list) - 1
        del self.list[lastindex]
        while self.heap and (self.heap[0] not in self.list):
            heapq.heappop(self.heap)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()