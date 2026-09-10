class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[ind + 1], nums[i] = nums[i], nums[ind + 1]
                ind += 1