class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pro = 1
        zero = 0
        zeroindex = []
        for i in range(0, len(nums)):
            if nums[i] is not 0:
                pro *= nums[i]
            else:
                zeroindex.append(i)
                zero += 1
        res = [0] * len(nums)
        if zero > 1:
            return res
        if zero == 1:
            res[zeroindex[0]] = pro
            return res
        for i in range(0, len(nums)):
            res[i] = pro//nums[i]
        return res