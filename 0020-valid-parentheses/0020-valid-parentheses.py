class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openpara = set(['(', '{', '['])
        closepara = {')': '(', '}': '{', ']': '['}
        for schar in s:
            if schar in openpara:
                stack.append(schar)
            else:
                if len(stack) == 0 or closepara[schar] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False