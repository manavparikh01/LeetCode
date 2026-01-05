class Solution:

    def __init__(self, w: List[int]):
        self.total = []
        total = 0
        for num in w:
            total += num
            self.total.append(total)
        self.value = total
        # total = sum(w)
        # totaltn = 0
        # self.hashmap = {}
        # self.arr = []
        # for i, num in enumerate(w):
        #     ratio = num / total * 100
        #     totaltn += ratio
        #     self.arr.append(totaltn)
        #     self.hashmap[totaltn] = i

    def pickIndex(self) -> int:
        pickvalue = random.randint(1, self.value)
        for i, num in enumerate(self.total):
            if pickvalue <= num:
                return i
        # predict = random.randint(1, 100)
        # for num in self.arr:
        #     if predict <= num:
        #         return self.hashmap[num]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()