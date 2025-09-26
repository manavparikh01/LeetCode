class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pcount = {}
        scount = {}
        for i in range(len(p)):
            pcount[p[i]] = 1 + pcount.get(p[i], 0)
            scount[s[i]] = 1 + scount.get(s[i], 0)
        
        res = [0] if pcount == scount else []
        l = 0
        for i in range(len(p), len(s)):
            scount[s[i]] = 1 + scount.get(s[i], 0)
            scount[s[l]] -= 1
            if scount[s[l]] == 0:
                scount.pop(s[l])
            l += 1
            if pcount == scount:
                res.append(l)
        return res