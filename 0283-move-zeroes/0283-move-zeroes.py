class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        i = 0
        while i < length:
            j = i
            if nums[j] == 0:
                while j < length:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
                length -= 1
            else:
                i += 1
        # length = len(nums)
        # l = 0
        # r = length - 1
        # while l < r:
        #     while l < r and nums[l] == 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     l += 1
