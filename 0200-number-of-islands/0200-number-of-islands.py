class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        def dp(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dp(i , j + 1)
            dp(i + 1, j)
            dp(i, j - 1)
            dp(i - 1, j)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    total += 1
                    dp(i, j)
        return total
