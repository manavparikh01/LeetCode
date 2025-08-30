class Solution:
    def countBits(self, n: int) -> List[int]:
        array = [0] * (n+1)
        for i in range(n + 1):
            res = 0
            if i == 0:
                array[i] = 0
                continue
            itemp = i
            while itemp:
                itemp &= (itemp - 1)
                res += 1
            array[i] = res
        return array