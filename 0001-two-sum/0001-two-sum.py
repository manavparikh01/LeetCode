class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i in range(0, len(nums)):
            if target - nums[i] in list:
                return [list[target-nums[i]], i]
            else:
                list[nums[i]] = i
        return []
            