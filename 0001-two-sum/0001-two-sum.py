class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storehash = {}
        result = []
        length = len(nums)
        for i in range(0, length):
            if target - nums[i] in storehash:
                result.append(storehash[target-nums[i]])
                result.append(i)
                return result
            else:
                storehash[nums[i]] = i
        return result