class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        countgrid = [[0 for _ in range(cols)] for _ in range(rows)]
        visitedgrid = [[False for _ in range(cols)] for _ in range(rows)]
        fincount = 0

        def dfs(i, j, count):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if grid[i][j] == 0 or (visitedgrid[i][j] == True and countgrid[i][j] <= count):
                return
            countgrid[i][j] = count
            visitedgrid[i][j] = True
            dfs(i - 1, j, count + 1)
            dfs(i, j + 1, count + 1)
            dfs(i + 1, j, count + 1)
            dfs(i, j - 1, count + 1)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dfs(i, j, 0)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visitedgrid[i][j] == False:
                    return -1
                fincount = max(fincount, countgrid[i][j])
        
        return fincount
