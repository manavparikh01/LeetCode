class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        temp = [[0 for i in range(COL)] for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                if i == 0 and j == 0:
                    temp[i][j] = grid[i][j]
                elif i == 0:
                    temp[i][j] = grid[i][j] + temp[i][j - 1]
                elif j == 0:
                    temp[i][j] = grid[i][j] + temp[i - 1][j]
                else:
                    temp[i][j] = grid[i][j] + min(temp[i][j - 1], temp[i - 1][j])
        return temp[ROW - 1][COL - 1]
