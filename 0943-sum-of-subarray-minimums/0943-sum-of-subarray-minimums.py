class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []
        for i, n in enumerate(arr):
            while stack and stack[-1][1] > n:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right) % MOD
            stack.append([i, n])
        return res