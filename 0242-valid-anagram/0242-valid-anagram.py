class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hamap = {}
        for i in s:
            if i not in hamap:
                hamap[i] = 1
            else:
                hamap[i] = hamap[i] + 1
        for j in t:
            if j not in hamap:
                return False
            else:
                if hamap[j] > 1:
                    hamap[j] = hamap[j] - 1
                else:
                    del hamap[j]
        if len(hamap) > 0:
            return False
        return True