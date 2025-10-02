class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        prev = 0
        res = 0
        currentoperation = "+"
        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1
                if currentoperation == "+":
                    res += curr
                    prev = curr
                elif currentoperation == "-":
                    res -= curr
                    prev = -curr
                elif currentoperation == "*":
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                else:
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                curr = 0
            elif curr_char != " ":
                currentoperation = curr_char
            i += 1
        return res
            