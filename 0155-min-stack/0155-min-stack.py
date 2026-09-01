class MinStack:

    def __init__(self):
        self.list = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        self.min = min(self.min, value)
        self.list.append([value, self.min])

    def pop(self) -> None:
        self.list.pop()
        if len(self.list) == 0:
            self.min = float('inf')
        else:
            self.min = self.list[-1][1]

    def top(self) -> int:
        return self.list[-1][0]

    def getMin(self) -> int:
        return self.list[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()