class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = "null"
        for num in nums:
            if count == 0:
                ele = num
                count += 1
            elif num == ele:
                count += 1
            else:
                count -= 1
        return ele
