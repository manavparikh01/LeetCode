class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the break point which breaks the upward curve from last index
        length = len(nums)
        brp = -1
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                brp = i
                break
        
        # if break point still -1, return reverse
        if brp == -1:
            nums.reverse()
            return nums
        
        # traverse again from last index to find the element larger than the break point
        for i in range(length - 1, brp, -1):
            if nums[i] > nums[brp]:
                nums[brp], nums[i] = nums[i], nums[brp]
                break
        
        # reverse the array from the break point + 1 index to last index
        nums[brp + 1:] = reversed(nums[brp + 1:])
        return nums
            
