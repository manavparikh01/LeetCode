class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        def dp(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dp(i, j + 1) + dp(i + 1, j) + dp(i, j - 1) + dp(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temparea = dp(i, j)
                    maxarea = max(maxarea, temparea)
        return maxarea