class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return -1