class Solution:
    def power(self, x:float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1.0:
            return 1
        if n % 2 == 0:
            return self.power(x*x, n//2)
        return x * self.power(x, n-1)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0/self.power(x, -n)
        return self.power(x, n)