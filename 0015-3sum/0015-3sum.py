class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortnums = sorted(nums)
        finallist = []
        for i, num in enumerate(sortnums):
            if i > 0 and sortnums[i] == sortnums[i - 1]:
                continue
            a = num
            l = i + 1
            r = len(sortnums) - 1
            while l < r:
                if a + sortnums[l] + sortnums[r] < 0:
                    l += 1
                elif a + sortnums[l] + sortnums[r] > 0:
                    r -= 1
                else:
                    finallist.append([a, sortnums[l], sortnums[r]])
                    l += 1
                    while sortnums[l] == sortnums[l - 1] and l < r:
                        l += 1
        return finallist
