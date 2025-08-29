class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        def rec(y, m):
            if m == 0:
                return 1
            pro = 0
            temp = rec(y, m//2)
            if m % 2 == 0:
                pro = temp * temp
            else:
                pro =  y * temp * temp
            return pro
        prod = 0
        if n < 0:
            prod = rec(1/x, -n)
        else:
            prod = rec(x, n)
        return prod