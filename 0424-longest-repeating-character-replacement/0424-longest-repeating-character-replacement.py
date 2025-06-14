class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0
        maxf = 0
        for h in range(len(s)):
            count[s[h]] = count.get(s[h], 0) + 1
            maxf = max(maxf, count[s[h]])
            while (h - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, h - l + 1)
        return res