class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = "+"
        i = 0
        while i < len(s):
            charat = s[i]
            if charat.isdigit():
                digit = 0
                while i < len(s) and s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                    i += 1
                i -= 1
                if operation == "+":
                    stack.append(int(digit))
                else:
                    stack.append(-int(digit))
            elif charat != " ":
                if charat == "+":
                    operation = "+"
                elif charat == "-":
                    operation = "-"
                elif charat == "(":
                    stack.append(operation)
                    stack.append(charat)
                    operation = "+"
                else:
                    currsum = 0
                    while stack[-1] != "(":
                        currsum += stack.pop()
                    stack.pop()
                    curroperation = stack.pop()
                    if curroperation == "+":
                        stack.append(currsum)
                    else:
                        stack.append(-currsum)
            i += 1
        return sum(stack)
                