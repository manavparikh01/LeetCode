class Solution:
    def countBits(self, n: int) -> List[int]:
        array = [0] * (n+1)
        for i in range(n + 1):
            array[i] = bin(i).count("1")
        return array