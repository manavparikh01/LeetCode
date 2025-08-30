class Solution:
    def reverseBits(self, n: int) -> int:
        bina = format(n, "032b")
        binarev = bina[::-1]
        return int(binarev, 2)