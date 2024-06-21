class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml = 0
        mb = 0
        l = len(matrix[0]) - 1
        l1 = l
        b = len(matrix) - 1
        while -1 < ml <= l and -1 < mb <= b:
            n = (ml + l)//2
            m = (mb + b)//2
            #print(ml, l, n, mb, b, m)
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                if matrix[m][0] > target:
                    b = m-1
                else:
                    l = n-1
            else:
                if matrix[m][l1] < target:
                    mb = m+1
                else:
                    ml = n+1
        return False