class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sone = ''.join(sorted(s))
        tone = ''.join(sorted(t))
        if sone == tone:
            return True
        return False