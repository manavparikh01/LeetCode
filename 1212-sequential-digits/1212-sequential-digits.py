class Solution:
    def minforlength(self, length: int) -> int:
        res = 0
        i = 1
        while i <= length:
            res = res * 10 + i
            i += 1
        return res
    def getnewstart(self, start: int) -> int:
        res = 0
        newres = 0
        while start > 0:
            digit = (start % 10) + 1
            res = res * 10 + digit
            start = start // 10
        while res > 0:
            digit = res % 10
            newres = newres * 10 + digit
            res = res // 10
        return newres
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lenoflow = len(str(abs(low)))
        start = self.minforlength(lenoflow)
        res = []
        while start <= high:
            if start >= low:
                res.append(start)
            if start % 10 == 9:
                lenoflow += 1
                start = self.minforlength(lenoflow)
            else:
                start = self.getnewstart(start)
        return res
            