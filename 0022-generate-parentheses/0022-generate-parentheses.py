class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dp(openn, closen):
            if openn == closen == n:
                res.append("".join(stack))
                return
            if openn <= n:
                stack.append("(")
                dp(openn + 1, closen)
                stack.pop()
            
            if closen < openn:
                stack.append(")")
                dp(openn, closen + 1)
                stack.pop()
        
        dp(0, 0)
        return res