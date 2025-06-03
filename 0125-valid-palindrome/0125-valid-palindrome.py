class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = lower(s)
        sclean = re.sub(r'[^a-z0-9]', '', s)
        l = 0
        h = len(sclean) - 1
        while h > l:
            if sclean[l] != sclean[h]:
                return False
            else:
                l += 1
                h -= 1
        return True