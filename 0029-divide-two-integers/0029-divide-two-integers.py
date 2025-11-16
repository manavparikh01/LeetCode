class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div = int(dividend/divisor)
        if div > (2 ** 31) - 1:
            return (2 ** 31) - 1
        if div < -(2 ** 31):
            return -(2 ** 31)
        return div