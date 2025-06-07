class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        max_water = 0
        while low < high:
            water = (high - low) * min(height[low], height[high])
            max_water = max(max_water, water)
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return max_water