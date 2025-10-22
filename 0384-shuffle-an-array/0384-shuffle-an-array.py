class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        diffarr = []
        solarr = self.arr.copy()
        while solarr:
            ran = random.randint(0, len(solarr) - 1)
            diffarr.append(solarr[ran])
            del solarr[ran]
        return diffarr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()