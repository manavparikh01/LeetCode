class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums2 = []
        for i in nums:
            nums2.append(1)
        maxi = 0;
        for i in range(len(nums) - 1, -1, -1):
            temp = [1]
            for j in range(i+1, len(nums), 1):
                if (nums[i] < nums[j]):
                    temp.append(1 + nums2[j])
                #print(temp, nums[i], nums[j])
            nums2[i] = max(temp)
            maxi = max(maxi, nums2[i])
        return maxi