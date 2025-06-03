class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        # sortresult = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = nums[i]
            fornow = {}
            for j in range(i+1, len(nums)):
                find = -(nums[j] + temp)
                if find in fornow:
                    templist = []
                    templist.append(temp)
                    templist.append(nums[j])
                    templist.append(find)
                    # sortlist = sorted(templist)
                    # if sortlist in sortresult:
                    #     continue
                    # else:
                        # sortresult.append(sortlist)
                    if templist not in result:
                        result.append(templist)
                else:
                    fornow[nums[j]] = j
        return result