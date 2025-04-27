class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        st = [0] * 26
        tt = [0] * 26

        for i in range(len(s)):
            st[ord(s[i]) - ord('a')] += 1
            tt[ord(t[i]) - ord('a')] += 1

        if st == tt:
            return True
        return False