class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        cur_rows = cur_cols = 0
        res = []
        going_up = True
        while len(res) < ROWS * COLS:
            if going_up:
                while cur_rows >= 0 and cur_cols < COLS:
                    res.append(mat[cur_rows][cur_cols])
                    cur_rows -= 1
                    cur_cols += 1
                if cur_cols == COLS:
                    cur_rows += 2
                    cur_cols -= 1
                else:
                    cur_rows += 1
                going_up = False
            else:
                while cur_rows < ROWS and cur_cols >= 0:
                    res.append(mat[cur_rows][cur_cols])
                    cur_rows += 1
                    cur_cols -= 1
                if cur_rows == ROWS:
                    cur_rows -= 1
                    cur_cols += 2
                else:
                    cur_cols += 1
                going_up = True
        return res
        