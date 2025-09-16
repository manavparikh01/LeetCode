class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix) - 1
        COL = len(matrix[0]) - 1
        r = 0
        while r <= ROW and COL >= 0:
            if matrix[r][COL] == target:
                return True
            if matrix[r][COL] < target:
                r += 1
            else:
                COL -= 1
        return False