class Solution:
    def isPrime(self, n: int) -> bool:
        i = 2
        res = 0
        while i*i <= n:
            if n % i == 0:
                res += 1
            i += 1
        return True if res == 1 else False
    
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
        def is_palindrome(x):
            return str(x) == str(x)[::-1]
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8
