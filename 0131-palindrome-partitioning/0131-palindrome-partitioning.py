class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def dp(i):
            if i >= len(s):
                res.append(temp.copy())
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    temp.append(s[i:j+1])
                    dp(j+1)
                    temp.pop()
            return
        dp(0)
        return res
        # res = []
        # temp = []
        # def dp(l, r):
        #     nonlocal res, temp
        #     print(l, r)
        #     if l == r:
        #         return
        #     if s[l:r] == s[l:r][::-1]:
        #         temp.append(s[l:r])
        #     for i in range(l + 1, r):
        #         dp(l, i)
        #         dp(i, r)
        #     res.append(temp.copy())
        #     return
        
        # dp(0, len(s))
        # return res
            