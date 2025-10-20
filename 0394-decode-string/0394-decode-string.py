class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                multi = ""
                while stack and stack[-1].isdigit():
                    multi = stack.pop() + multi
                finalstring = int(multi) * string
                stack.append(finalstring)
        return ''.join(stack)