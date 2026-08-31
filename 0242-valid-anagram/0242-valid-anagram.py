class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for schar in s:
            if schar in hashmap:
                hashmap[schar] = hashmap[schar] + 1
            else:
                hashmap[schar] = 1
        for tchar in t:
            if tchar not in hashmap:
                return False
            hashmap[tchar] = hashmap[tchar] - 1
            if hashmap[tchar] == 0:
                del hashmap[tchar]
        if len(hashmap) == 0:
            return True
        return False