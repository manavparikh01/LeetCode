class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        for i in range(ROW - 1):
            for j in range(COL - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

