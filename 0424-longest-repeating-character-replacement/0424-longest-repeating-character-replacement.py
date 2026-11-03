class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        rescount = 0
        l = 0
        for i in range(len(s)):
            hashmap[s[i]] += 1
            while (i - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            rescount = max(rescount, i - l + 1)
        return rescount