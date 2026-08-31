class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        out = float('inf')
        for key in count:
            if count[key] == 1:
                out = min(out, s.find(key))
        if out < len(s):
            return out
        return -1

        