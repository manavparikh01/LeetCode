class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        man = 0
        for i in range(0, len(nums), 1):
            man = i
            for j in range(i+1, len(nums), 1):
                if nums[j] < nums[man]:
                    man = j
            nums[i], nums[man] = nums[man], nums[i]
            
        