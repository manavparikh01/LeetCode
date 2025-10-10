class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix) - 1
        COL = len(matrix[0]) - 1
        temp = {}
        def dfs(r, c):
            if r > ROW or c > COL:
                return 0
            if (r, c) not in temp:
                down = dfs(r + 1, c)
                right = dfs(r, c + 1)
                diag = dfs(r + 1, c + 1)
                temp[(r, c)] = 0
                if matrix[r][c] == "1":
                    temp[(r, c)] = 1 + min(down, right, diag)

            return temp[(r, c)]
        dfs(0, 0)
        return max(temp.values()) ** 2