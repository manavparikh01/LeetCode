class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        arr = []
        for i in s:
            if i == "(":
                arr.append(i)
                count += 1
            elif i == ")":
                if count > 0:
                    count -= 1
                    arr.append(i)
            else:
                arr.append(i)
        r = len(arr) - 1
        while count > 0:
            while r >= 0 and arr[r] != "(":
                r -= 1
            del arr[r]
            r -= 1
            count -= 1
        return ''.join(arr)
        # maxlength = 0
        # res = ""
        # def dp(arr, i, l_c, r_c):
        #     nonlocal maxlength, res, s
        #     if i == len(s):
        #         if l_c == r_c and len(arr) > maxlength:
        #             res = ''.join(arr)
        #             maxlength = len(arr)
        #         return
        #     if len(arr) <= maxlength - (len(s) - i - 1):
        #         return
        #     if s[i] == "(":
        #         arr.append(s[i])
        #         dp(arr, i + 1, l_c + 1, r_c)
        #         arr.pop()
        #         dp(arr, i + 1, l_c, r_c)
        #     elif s[i] == ")":
        #         if r_c < l_c:
        #             arr.append(s[i])
        #             dp(arr, i + 1, l_c, r_c + 1)
        #             arr.pop()
        #         dp(arr, i + 1, l_c, r_c)
        #     else:
        #         arr.append(s[i])
        #         dp(arr, i + 1, l_c, r_c)
        # dp([], 0, 0, 0)
        # return res