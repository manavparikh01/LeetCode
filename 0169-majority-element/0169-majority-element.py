class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        length = len(nums)
        if length < 3:
            return nums[0]
        for i in nums:
            if i in map:
                map[i] = map[i]+1
                if map[i] > length/2:
                    return i
            else:
                map[i] = 1
        return -1