class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lone = len(haystack)
        ltwo = len(needle)
        i = 0
        j = 0
        while i < lone and j < ltwo:
            if haystack[i] != needle[j]:
                i += 1
            else:
                start = i
                while j < ltwo and i < lone and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == ltwo:
                    return start
                j = 0
                i = start + 1
        return -1