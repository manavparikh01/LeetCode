class Solution:
    def numberOfWays(self, s: str) -> int:
        zerolr = [0] * len(s)
        zerorl = [0] * len(s)
        onelr = [0] * len(s)
        onerl = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] == "0":
                zerolr[i] = zerolr[i - 1] + 1
                onelr[i] = onelr[i - 1]
            else:
                onelr[i] = onelr[i - 1] + 1
                zerolr[i] = zerolr[i - 1]
        for i in range(len(s) - 2, -1, -1):
            if s[i + 1] == "0":
                zerorl[i] = zerorl[i + 1] + 1
                onerl[i] = onerl[i + 1]
            else:
                onerl[i] = onerl[i + 1] + 1
                zerorl[i] = zerorl[i + 1]
        for i in range(1, len(s) - 1):
            temp = 0
            if s[i] == "0":
                temp = onelr[i] * onerl[i]
            else:
                temp = zerolr[i] * zerorl[i]
            res += temp
        return res
        # back tracking approach
        # ways = 0
        # def dp(index, arr):
        #     nonlocal ways
        #     if len(arr) > 1 and s[index] == arr[-2]:
        #         return
        #     if len(arr) == 3:
        #         ways += 1
        #         return
        #     for i in range(index, len(s)):
        #         newarr = arr + s[i]
        #         dp(i, newarr)
        #     return
        # dp(0, "")
        # return ways