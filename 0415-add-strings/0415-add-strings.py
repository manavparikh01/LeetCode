class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        while i >= 0 or j >= 0 or carry > 0:
            numa = int(num1[i]) if i >= 0 else 0
            numb = int(num2[j]) if j >= 0 else 0
            total = numa + numb + carry
            digit = total % 10
            carry = total // 10
            res = str(digit) + res
            i -= 1
            j -= 1
        return res