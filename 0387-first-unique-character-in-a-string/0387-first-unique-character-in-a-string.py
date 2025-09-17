class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] = hashmap[char] + 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
