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
        string = str(n)
        l = 0
        r = len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    def primePalindrome(self, n: int) -> int:
        if n < 2:
            return 2
        if 8 <= n <= 11:
            return 11
        while True:
            s = len(str(n))
            if s % 2 == 0:
                n = 10 ** s
                continue
            if self.isPrime(n) and self.isPalindrome(n):
                return n
            else:
                n += 1