class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        i = 0
        for i in range(len(operations)):
            if operations[i][0] != "-":
                if operations[i].isdigit():
                    stack.append(int(operations[i]))
                else:
                    if operations[i] == "C":
                        stack.pop()
                    elif operations[i] == "D":
                        top = stack[-1]
                        stack.append(2 * top)
                    elif operations[i] == "+":
                        last = stack[-1]
                        slast = stack[-2]
                        stack.append(last + slast)
            else:
                stack.append(-int(operations[i][1:]))
        return sum(stack)