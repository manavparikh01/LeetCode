class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i=0
        j=0
        total = 0
        arr = [[-1 for j in range(n)] for i in range(m)]
        def df(i, j, total, arr):
            if arr[i][j] != -1:
                return arr[i][j]
            if i == m-1 or j == n-1:
                total = total + 1
                return total
            temp1 = df(i+1, j, total, arr)
            temp2 = df(i, j+1, total, arr)
            arr[i][j] = temp1 + temp2
            return arr[i][j]
        total = df(0,0,0, arr)
        # arr[m][n] = 0
        # total = df(0,0, 0)
        # for i in range(0,m):
        #     for j in range(0,n):
                
        return total