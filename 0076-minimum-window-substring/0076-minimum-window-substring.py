class Solution(object):
    # def checkdict(sdict, tdict):
    #     for indx, val in sdict.items():
    #         if tdict[indx] > val:
    #             return False
    #     return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""
        tdict = {}
        sdict = {}
        l = 0
        have = 0
        res = [-1, -1]
        reslen = float("infinity")
        for i in range(len(t)):
            tdict[t[i]] = tdict.get(t[i], 0) + 1
        need = len(tdict)
        for h in range(len(s)):
            sdict[s[h]] = sdict.get(s[h], 0) + 1
            if s[h] in tdict and sdict[s[h]] == tdict[s[h]]:
                have += 1
            while have == need:
                if (h - l + 1) < reslen:
                    res = [l, h]
                    reslen = h - l + 1
                sdict[s[l]] -= 1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1
        return s[res[0] : res[1] + 1] if reslen != float("infinity") else ""

        