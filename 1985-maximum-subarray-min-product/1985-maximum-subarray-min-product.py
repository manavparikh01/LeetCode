class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        prefix = [0]
        minpro = 0
        for i in nums:
            prefix.append(prefix[-1] + i)
        
        for i, value in enumerate(nums):
            startpoint = i
            while stack and stack[-1][1] > value:
                start, val = stack.pop()
                minpro = max(minpro, (prefix[i] - prefix[start]) * val)
                startpoint = start
            stack.append([startpoint, value])
        
        for i, val in stack:
            minpro = max(minpro, (prefix[len(nums)] - prefix[i]) * val)
        
        return minpro % (10**9 + 7)