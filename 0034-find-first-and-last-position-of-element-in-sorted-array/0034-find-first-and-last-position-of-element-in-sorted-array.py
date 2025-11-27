class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            res = (l + r) // 2
            if nums[res] == target:
                temp = res
                while temp >= l and nums[temp] == target:
                    temp -= 1
                temp1 = res
                while temp1 <= r and nums[temp1] == target:
                    temp1 += 1
                return [temp + 1, temp1 - 1]
            elif nums[res] > target:
                r = res - 1
            else:
                l = res + 1
        return [-1, -1]