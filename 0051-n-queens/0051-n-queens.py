class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diagonal_down = set()
        diagonal_up = set()
        board = [["."] * n for i in range(n)]
        res = []
        def dp(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if c in col or r-c in diagonal_down or r+c in diagonal_up:
                    continue
                col.add(c)
                diagonal_down.add(r-c)
                diagonal_up.add(r+c)
                board[r][c] = "Q"
                dp(r+1)
                col.remove(c)
                diagonal_down.remove(r-c)
                diagonal_up.remove(r+c)
                board[r][c] = "."
        dp(0)
        return res
        # final = []
        # total_q = 0
        # res = []
        # string = ""
        # def putQat(i, j):
        #     # back
        #     for x in range(0, n):
        #         temp[x][j] = False
        #     # top
        #     for y in range(0, n):
        #         temp[i][y] = False
        #     # down
        #     x,y = i,j
        #     while x - 1 >= 0 and y - 1 >= 0:
        #         x -= 1
        #         y -= 1
        #         temp[x][y] = False
        #     x1,y1 = i,j
        #     while x - 1 >= 0 and y + 1 < n:
        #         x -= 1
        #         y += 1
        #         temp[x][y] = False
        #     x2,y2 = i,j
        #     while x + 1 < n and y - 1 >= 0:
        #         x += 1
        #         y -= 1
        #         temp[x][y] = False
        #     x3,y3 = i,j
        #     while x + 1 < n and y + 1 < n:
        #         x += 1
        #         y += 1
        #         temp[x][y] = False

        # def dp(i, j):
        #     if temp[i][j] = False:
        #         string += "."
        #         return
            
        #     for x in range(i, n):
        #         for y in range(j, n):
        #             putQat(x, y)
        #             string += "Q"
        #             total_q += 1
        #             dp(x, y)
        #         res.append(string)
        #         string = ""
        
        # for x in range(0, n):
        #     for y in range(0, n):
                
        #         dp(x,y)
        #         if total_q = n:
        #             final.append(res)