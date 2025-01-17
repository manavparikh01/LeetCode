class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        def partitionHelper(index):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    partitionHelper(i + 1)
                    path.pop()


        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        partitionHelper(0)
        return res
