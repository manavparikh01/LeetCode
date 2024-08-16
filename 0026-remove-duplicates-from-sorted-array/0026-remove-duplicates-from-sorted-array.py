class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 0
        j = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[j]:
                i += 1
            count += 1
            if j+1 < len(nums) and i == len(nums):
                nums[j+1] = nums[i-1]
            else:
                if j+1 < len(nums):
                    nums[j+1] = nums[i]
            j = j+1
        return count