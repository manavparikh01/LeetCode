class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        numsu = set(nums)
        length = 1
        for i in numsu:
            slength = 1
            if i - 1 in numsu:
                continue
            while i + 1 in numsu:
                slength += 1
                i = i+1
            length = max(length, slength)
        return length
