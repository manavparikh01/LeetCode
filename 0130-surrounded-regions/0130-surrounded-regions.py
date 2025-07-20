class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dp(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == "X" or (i, j) in visited:
                return
            visited.add((i, j))
            dp(i, j + 1)
            dp(i + 1, j)
            dp(i, j - 1)
            dp(i - 1, j)
            return

        for i in range(rows):
            dp(i, 0)
            dp(i, cols - 1)
        
        for j in range(cols):
            dp(0, j)
            dp(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        # rows = len(board)
        # cols = len(board[0])
        # visited = set()
        # conedge = set()
        # def dp(i, j):
        #     if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in conedge:
        #         return True
        #     if (i, j) in visited or board[i][j] == "X":
        #         return False
        #     visited.add((i, j))
        #     if dp(i, j + 1) or dp(i + 1, j) or dp(i ,j - 1) or dp(i - 1, j):
        #         conedge.add((i, j))
        #         return True
        #     board[i][j] = "X"
        #     return False
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j] == "O":
        #             dp(i, j)