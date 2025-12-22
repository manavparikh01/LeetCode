class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        arr = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        res = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    for m, n in arr:
                        im = i + m
                        jn = j + n
                        if im < 0 or im >= ROW or jn < 0 or jn >= COL:
                            res += 1
                        elif grid[im][jn] == 0:
                            res += 1
        return res