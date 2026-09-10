class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for indx, schar in enumerate(s):
            if count[schar] == 1:
                return indx
        return -1
        