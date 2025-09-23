class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            index = self.hashmap[val]
            lastval = self.arr[-1]
            self.arr[index] = lastval
            self.arr.pop()
            self.hashmap[lastval] = index
            return True
        return False

    def getRandom(self) -> int:
        ran = random.randint(0, len(self.arr) - 1)
        return self.arr[ran]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()