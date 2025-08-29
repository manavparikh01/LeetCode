class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10
        res = res[::-1]
        des = 0
        while des < len(res) and res[des] == 0:
            des += 1
        res = map(str, res[des:])
        return "".join(res)