class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        lena = len(a) - 1
        lenb = len(b) - 1
        res = ""
        while lena >= 0 and lenb >= 0:
            sumab = int(a[lena]) + int(b[lenb]) + carry
            if sumab == 2:
                res = "0" + res
                carry = 1
            elif sumab == 3:
                res = "1" + res
                carry = 1
            else:
                res = str(sumab) + res
                carry = 0
            lena -= 1
            lenb -= 1
        while lena >= 0:
            sumab = int(a[lena]) + carry
            if sumab == 2:
                res = "0" + res
                carry = 1
            elif sumab == 3:
                res = "1" + res
                carry = 1
            else:
                res = str(sumab) + res
                carry = 0
            lena -= 1
        while lenb >= 0:
            sumab = int(b[lenb]) + carry
            if sumab == 2:
                res = "0" + res
                carry = 1
            elif sumab == 3:
                res = "1" + res
                carry = 1
            else:
                res = str(sumab) + res
                carry = 0
            lenb -= 1
        if carry == 1:
            res = "1" + res
        return res