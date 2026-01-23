class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlength = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                temp += 1
            else:
                maxlength = max(maxlength, temp)
                temp = 1
        maxlength = max(maxlength, temp)
        return maxlength