class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        found = False

        def dp(i, j, ind):
            nonlocal temp, found
            
            if ind >= len(word):
                found = True
                return 
            if found == True or i >= rows or i < 0 or j >= cols or j < 0 or temp[i][j] == True or board[i][j] != word[ind]:
                return
            temp[i][j] = True
            ind += 1
            dp(i, j + 1, ind)
            dp(i + 1, j, ind)
            dp(i, j - 1, ind)
            dp(i - 1, j, ind)
            temp[i][j] = False
            return

        for i in range(rows):
            for j in range(cols):
                temp = [[False for _ in range(cols)] for _ in range(rows)]
                if found == False and board[i][j] == word[0]:
                    dp(i, j, 0)

        return found