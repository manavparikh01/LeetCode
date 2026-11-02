class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1, 2, 6, 24]
        # [24, 24, 12, 4]
        left_product = [[] for _ in range(len(nums) + 1)]
        right_product = [[] for _ in range(len(nums) + 1)]
        left_product[0] = 1
        right_product[len(nums)] = 1
        for i in range(0, len(nums)):
            left_product[i + 1] = left_product[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i]
        finallist = []
        for i in range(len(nums)):
            finallist.append(left_product[i] * right_product[i + 1])
        return finallist