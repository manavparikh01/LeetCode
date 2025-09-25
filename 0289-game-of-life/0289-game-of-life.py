class Solution:
    def in_bounds(self, r, c, ROW, COL):
        return 0 <= r < ROW and 0 <= c < COL

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        res = [[0] * COL for _ in range(ROW)]
        arr = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        boundaryforr = [0, ROW - 1]
        boaundaryforc = [0, COL -1]
        for i in range(ROW):
            for j in range(COL):
                countofone = 0
                for r, c in arr:
                    nr, nc = r + i, c + j
                    if self.in_bounds(nr, nc, ROW, COL):
                        if board[nr][nc] == 1:
                            countofone += 1
                if countofone < 2 or countofone > 3:
                    res[i][j] = 0
                elif countofone == 3:
                    res[i][j] = 1
                else:
                    res[i][j] = board[i][j]
        for i in range(ROW):
            for j in range(COL):
                board[i][j] = res[i][j]                