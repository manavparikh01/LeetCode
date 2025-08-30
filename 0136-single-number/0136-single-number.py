class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        for key, val in hashmap.items():
            if val == 1:
                return key