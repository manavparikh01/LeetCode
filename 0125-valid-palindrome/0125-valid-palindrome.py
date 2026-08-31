class Solution:
    def isPalindrome(self, s: str) -> bool:
        se = re.sub(r'[^a-z0-9]', '', s.lower())
        l, h = 0, len(se) - 1
        while l < h:
            if se[l] != se[h]:
                return False
            l += 1
            h -= 1
        return True