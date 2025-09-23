class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr.append(val)
            self.length += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        ran = random.randint(0, self.length - 1)
        return self.arr[ran]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()