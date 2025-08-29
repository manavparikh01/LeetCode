class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def contoInt(s):
            num = 0
            for i in s:
                num = num * 10 + int(i)
            return num
        pro = contoInt(num1) * contoInt(num2)
        return str(pro)