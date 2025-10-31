class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        ROW = len(board)
        COL = len(board[0])
        arr = [[0] * COL for _ in range(ROW)]
        points = [(-1, 0), (-1, 1), (0 ,1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "M":
                    arr[i][j] = -1
                    for m, n in points:
                        ni, nj = i + m, j + n
                        if ni < 0 or nj < 0 or ni == ROW or nj == COL or board[ni][nj] != "E":
                            continue
                        arr[ni][nj] += 1
                elif board[i][j].isdigit():
                    arr[i][j] = int(board[i][j])
                else:
                    continue
        visit = set()
        def clickme(i, j):
            if i < 0 or j < 0 or i == ROW or j == COL or board[i][j].isdigit() or (i, j) in visit:
                return
            if arr[i][j] > 0:
                board[i][j] = str(arr[i][j])
                return
            board[i][j] = "B"
            visit.add((i, j))
            for m, n in points:
                clickme(i + m, j + n)
            return
        
        clickme(click[0], click[1])
        return board
