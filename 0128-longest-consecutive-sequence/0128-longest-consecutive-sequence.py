class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        maxq = 1;
        j = 0
        small = float('-inf')
        for i in range(len(nums)):
            if nums[i] - 1 == small:
                j = j+1
                small = nums[i]
                
            elif nums[i] != small:
                small = nums[i]
                j = 1
            maxq = max(maxq,j)
        return maxq
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums) == 0:
        #     return 0
        # if min(nums) < 0:
        #     list = [0] * (max(nums) - min(nums) + 1)
        #     for i in nums:
        #         i = i - min(nums)
        #         list[i] = list[i] + 1
        # else:
        #     list = [0] * (max(nums) + 1)
        #     for i in nums:
        #         list[i] = list[i] + 1
        # i = 1
        # j = 1
        # maxi = 1
        # while i < len(list):
        #     while i < len(list) and list[i] > 0 and list[i-1] > 0:
        #         j = j + 1
        #         print(i, j)
        #         i = i + 1
        #     maxi = max(j, maxi)
        #     i = i + 1
        #     j = 1
        # return maxi