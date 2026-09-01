class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        total = 0
        count = 0
        for i, num in enumerate(nums):
            total += num
            prefix_sum[i] = total
        hashmap = defaultdict(int)
        for i in prefix_sum:
            if i == k:
                count += 1
            if i - k in hashmap:
                count += hashmap[i - k]
            hashmap[i] += 1
        return count
