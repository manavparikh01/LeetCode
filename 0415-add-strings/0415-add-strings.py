class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        while i >= 0 and j >= 0:
            total = int(num1[i]) + int(num2[j]) + carry
            digit = total % 10
            carry = total // 10
            res = str(digit) + res
            i -= 1
            j -= 1
        while i >= 0:
            total = int(num1[i]) + carry
            digit = total % 10
            carry = total // 10
            res = str(digit) + res
            i -= 1
        while j >= 0:
            total = int(num2[j]) + carry
            digit = total % 10
            carry = total // 10
            res = str(digit) + res
            j -= 1
        if carry > 0:
            res = str(carry) + res
        return res