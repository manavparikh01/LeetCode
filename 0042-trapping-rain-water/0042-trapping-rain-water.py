class Solution:
    def trap(self, height: List[int]) -> int:
        maxltor = [0] * len(height)
        for i in range(1, len(height)):
            maxltor[i] = max(maxltor[i - 1], height[i - 1])
        maxrtol = [0] * len(height)
        for i in range(len(height) - 1 - 1, -1, -1):
            maxrtol[i] = max(maxrtol[i + 1], height[i + 1])
        res = 0
        for i in range(len(height)):
            water = min(maxltor[i], maxrtol[i]) - height[i]
            if water > 0:
                res += water
        return res