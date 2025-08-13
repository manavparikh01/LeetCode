class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        # recursion based greedy
        # if len(nums) == 1:
        #     return True
        # def dfs(i):
        #     jumps = nums[i]
        #     for j in range(jumps, 0, -1):
        #         if i + j >= len(nums) - 1:
        #             return True
        #         if dfs(i + j):
        #             return True
        #     return False
        # return dfs(0)
        # dp - tle
        # temp = [False] * len(nums)
        # temp[len(nums) - 1] = True
        # for i in range(len(nums) - 2, -1, -1):
        #     for j in range(nums[i], 0, -1):
        #         if i + j >= len(nums):
        #             continue
        #         temp[i] = temp[i + j]
        #         if temp[i]:
        #             break
        # return temp[0]
