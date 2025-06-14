class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        somelist = set()
        l = 0
        res = 0
        for h in range(len(s)):
            while s[h] in somelist:
                somelist.remove(s[l])
                l += 1
            somelist.add(s[h])
            res = max(res, h - l + 1)
        return res
