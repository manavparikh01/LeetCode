class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(0, len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        