class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        for schar in s:
            if len(stack) == 0:
                stack.append(schar)
            else:
                if schar in hashmap:
                    if stack[-1] == hashmap[schar]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(schar)
        return len(stack) == 0