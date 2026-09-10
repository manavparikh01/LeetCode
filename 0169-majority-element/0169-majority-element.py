class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        mid = (len(nums) + 1) // 2
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] == mid:
                return num