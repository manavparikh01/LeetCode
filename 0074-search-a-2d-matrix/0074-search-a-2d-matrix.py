class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix) - 1
        COL = len(matrix[0]) - 1 
        lr, lc = 0, 0
        hr, hc = ROW, COL
        while lr <= hr and lc <= hc:
            midr = (lr + hr) // 2
            midc = (lc + hc) // 2
            if matrix[midr][midc] == target:
                return True
            elif target < matrix[midr][midc]:
                if target < matrix[midr][lc]:
                    hr = midr - 1
                else:
                    lr = midr
                    hr = midr
                    hc = midc - 1
            else:
                if target > matrix[midr][hc]:
                    lr = midr + 1
                else:
                    hr = midr
                    lc = midr
                    lc = midc + 1
        return False

