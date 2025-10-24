class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack.append(token)
        def callstack() -> int:
            nonlocal stack
            operation = stack.pop()
            if operation.isdigit():
                return int(operation)
            if len(operation) > 1 and operation[0] == "-":
                return int(operation)
            vala = callstack()
            valb = callstack()
            if operation == "+":
                return valb + vala
            elif operation == "-":
                return valb - vala
            elif operation == "*":
                return valb * vala
            else:
                return int(valb / vala)
        return callstack()