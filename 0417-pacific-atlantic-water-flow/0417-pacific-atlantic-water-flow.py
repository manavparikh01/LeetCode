class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        tempp = [[False for _ in range(cols)] for _ in range(rows)]
        tempa = [[False for _ in range(cols)] for _ in range(rows)]
        visitp = [[False for _ in range(cols)] for _ in range(rows)]
        visita = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            tempp[i][0] = True
            tempa[i][cols - 1] = True
        for j in range(cols):
            tempp[0][j] = True
            tempa[rows - 1][j] = True

        def dpp(i, j, height):
            nonlocal visitp
            if i < 0 or i >= rows or j < 0 or j >= cols or visitp[i][j] == True or heights[i][j] < height:
                return
            tempp[i][j] = True
            visitp[i][j] = True
            # print(i, j, height)
            dpp(i, j + 1, heights[i][j])
            dpp(i + 1, j, heights[i][j])
            dpp(i, j - 1, heights[i][j])
            dpp(i - 1, j, heights[i][j])
            return
        
        def dpa(i, j, height):
            nonlocal visita
            if i < 0 or i >= rows or j < 0 or j >= cols or visita[i][j] == True or heights[i][j] < height:
                return
            tempa[i][j] = True
            visita[i][j] = True
            dpa(i, j + 1, heights[i][j])
            dpa(i + 1, j, heights[i][j])
            dpa(i, j - 1, heights[i][j])
            dpa(i - 1, j, heights[i][j])
            return
        
        for i in range(rows):
            for j in range(cols):
                # print(i, j, tempp[i][j])
                if tempp[i][j] == True:
                    dpp(i, j, heights[i][j])
                if tempa[i][j] == True:
                    dpa(i, j, heights[i][j])
        
        for i in range(rows):
            for j in range(cols):
                if tempp[i][j] and tempa[i][j]:
                    res.append([i, j])

        return res