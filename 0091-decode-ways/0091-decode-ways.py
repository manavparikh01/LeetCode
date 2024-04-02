class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }
        #print(dp)
        def dpp(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dpp(i+1)
            
            if ((i+1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dpp(i+2)
                
            dp[i] = res
            #print(dp)
            return res
        
        return dpp(0)