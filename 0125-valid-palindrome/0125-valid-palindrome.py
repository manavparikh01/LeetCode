class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stext = ''.join(c for c in s if c.isalnum())
        print(stext)
        return stext.lower() == stext[::-1].lower()