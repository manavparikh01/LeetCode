class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []
        for i, n in enumerate(arr):
            while stack and stack[-1][1] > n:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = res + m * left * right
            stack.append([i, n])
        return res
    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        res = 0
        arr = [float("inf")] + arr + [float("inf")]
        stack = []
        for i, n in enumerate(arr):
            while stack and stack[-1][1] < n:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = res + m * left * right
            stack.append([i, n])
        return res
    def subArrayRanges(self, nums: List[int]) -> int:
        print(self.sumSubarrayMins(nums))
        print(self.sumSubarrayMaxs(nums))
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)