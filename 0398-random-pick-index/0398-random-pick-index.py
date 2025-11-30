class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in self.hashmap:
                self.hashmap[nums[i]] = [i]
            else:
                self.hashmap[nums[i]].append(i)

    def pick(self, target: int) -> int:
        length = len(self.hashmap[target])
        rand = random.randint(0, length - 1)
        return self.hashmap[target][rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)