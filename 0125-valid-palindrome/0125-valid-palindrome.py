class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub(r'[^a-z0-9]', '', s.lower())
        l = 0
        h = len(s_clean) - 1
        while l < h:
            if s_clean[l] != s_clean[h]:
                return False
            l += 1
            h -= 1
        return True