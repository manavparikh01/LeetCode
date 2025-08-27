class Solution:
    def isHappy(self, n: int) -> bool:
        totalSums = set()
        totalSums.add(n)
        def sumSquared(num):
            sumone = 0
            while num > 0:
                digit = num % 10
                sumone += digit**2
                num //= 10
            return sumone
        while n != 1:
            n = sumSquared(n)
            if n in totalSums:
                return False
            else:
                totalSums.add(n)
        return True
        
        