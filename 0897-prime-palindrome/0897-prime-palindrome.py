class Solution:
    def isPrime(self, n: int) -> bool:
        i = 2
        res = 0
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
    def isPalindrome(self, n: int) -> bool:
        return str(n) == str(n)[::-1]

    def primePalindrome(self, n: int) -> int:
        if n < 2:
            return 2
        if 8 <= n <= 11:
            return 11
        while True:
            if 10**7 < n < 10**8:
                n = 10**8
            if self.isPalindrome(n) and self.isPrime(n):
                return n
            n += 1