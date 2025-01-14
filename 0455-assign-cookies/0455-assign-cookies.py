class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        leng = len(g)
        lens = len(s)
        i = 0
        j = 0
        temp = 0
        while i < leng and j < lens:
            if s[j] >= g[i]:
                i = i + 1
                j = j + 1
                temp = temp + 1
            else:
                j = j + 1
        return temp
