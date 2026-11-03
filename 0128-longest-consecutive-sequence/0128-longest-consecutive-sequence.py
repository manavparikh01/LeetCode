class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setnums = set(nums)
        maxcount = 0
        for num in setnums:
            if num - 1 in setnums:
                continue
            else:
                count = 1
                while num + 1 in setnums:
                    count += 1
                    num = num + 1
                maxcount = max(maxcount, count)
        return maxcount