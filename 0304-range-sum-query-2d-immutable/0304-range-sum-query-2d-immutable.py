class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROW = len(matrix)
        COL = len(matrix[0])
        self.arr = [[0] * COL for _ in range(ROW)]
        res = 0
        for i in range(ROW):
            for j in range(COL):
                self.arr[i][j] = self.matrix[i][j] + res
                res = self.arr[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        while row1 <= row2:
            res += self.arr[row1][col2] - self.arr[row1][col1] + self.matrix[row1][col1]
            row1 += 1
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)