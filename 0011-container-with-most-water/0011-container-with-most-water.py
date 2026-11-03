class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 1, 7 -> 8, 7 -> 
        l = 0
        h = len(height) - 1
        maxarea = 0
        while l < h:
            maxarea = max(maxarea, min(height[l], height[h]) * (h - l))
            if height[h] >= height[l]:
                l += 1
            else:
                h -= 1
        return maxarea