class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and dictionary[s[i]] < dictionary[s[i + 1]]:
                res -= dictionary[s[i]]
            else:
                res += dictionary[s[i]]
        return res