class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set([])
        ata = set([])
        res = []

        def dfs(r, c, visited, prevheight):
            if ((r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevheight):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            return

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, ata, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, ata, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in ata:
                    res.append([r, c])
        
        return res