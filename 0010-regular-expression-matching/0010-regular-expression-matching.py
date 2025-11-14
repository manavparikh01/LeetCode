class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        hashmap = {}
        def dp(i, j):
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j < len(p) - 1 and p[j + 1] == "*":
                hashmap[(i, j)] = (dp(i, j + 2) or (match and dp(i + 1, j)))
                return hashmap[(i, j)]
            else:
                hashmap[(i, j)] = match and dp(i + 1, j + 1)
                return hashmap[(i, j)]
            hashmap[(i, j)] = False
            return hashmap[(i, j)]
        return dp(0, 0)