class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count, countT = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        have, need = 0, len(countT)
        window = [-1, -1]
        reslen = float("inf")
        l = 0
        for i in range(len(s)):
            c = s[i]
            count[c] += 1
            if c in countT and count[c] == countT[c]:
                have += 1
            while have == need:
                if (i - l + 1) < reslen:
                    window = [l, i]
                    reslen = i - l + 1
                count[s[l]] -= 1
                if s[l] in countT and count[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, i = window
        return s[l : i + 1] if reslen != float("inf") else ""
            
