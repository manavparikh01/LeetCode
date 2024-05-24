class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        if numRows == 3:
            return [[1],[1,1],[1,2,1]]
        li = [1,2,1];
        lii = [[1],[1,1],[1,2,1]];
        for i in range(3, numRows, 1):
            li2 = [1]
            for j in range(1,len(li),1):
                li2.append(li[j-1] + li[j])
            li2.append(1)
            li = li2
            lii.append(li2)
        return lii
            
                    
        