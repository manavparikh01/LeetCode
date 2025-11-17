class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = { 0: -1 }
        total = 0
        for i, num in enumerate(nums):
            total += num
            remain = total % k
            if remain not in hashmap:
                hashmap[remain] = i
            elif i - hashmap[remain] >= 2:
                return True
        return False