class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visitedarr = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        def dfs(i, j, grid):
            nonlocal visitedarr, rows, cols
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if grid[i][j] == '0' or visitedarr[i][j] == True:
                return
            visitedarr[i][j] = True
            dfs(i - 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0' or visitedarr[i][j] == True:
                    continue
                dfs(i, j, grid)
                count += 1
        
        return count