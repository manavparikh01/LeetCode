class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        li = [1]
        fin_li = [li]
        for i in range(1, numRows):
            temp_li = [1]
            for j in range(1, i):
                temp_li.append(fin_li[i-1][j-1] + fin_li[i-1][j])
            temp_li.append(1)
            fin_li.append(temp_li)
        return fin_li
