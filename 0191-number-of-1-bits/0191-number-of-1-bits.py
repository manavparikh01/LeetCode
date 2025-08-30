class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        count = 0
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        for i in binary:
            if i == "1":
                count += 1
        return count