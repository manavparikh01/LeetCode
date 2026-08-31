class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for schar in s:
            if schar.isalnum():
                string += schar.lower()
        return string == string[::-1]