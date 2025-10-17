class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(n)] for j in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                left, down = -1, -1
                if j == n - 1:
                    left = 0
                else:
                    left = arr[i][j + 1]
                if i == m - 1:
                    down = 0
                else:
                    down = arr[i + 1][j]
                arr[i][j] = max(1, left + down)
        return arr[0][0]