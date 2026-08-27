class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        count = 0
        for j in range(0, len(s)):
            if i == len(g):
                return count
            if s[j] >= g[i]:
                count += 1
                i += 1
        return count