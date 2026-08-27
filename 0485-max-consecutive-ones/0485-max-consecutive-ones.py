class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 0
        return max(maxcount, count)