class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashmap = defaultdict(int)
        l = 0
        maxsubstring = 1
        hashmap[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # the substring restarts
                maxsubstring = max(maxsubstring, i - l)
                l = i
                hashmap[s[i]] = i
            else:
                if s[i] not in hashmap:
                    hashmap[s[i]] = i
                else:
                    # in hashmap within the window
                    if hashmap[s[i]] >= l:
                        # print(l)
                        maxsubstring = max(maxsubstring, i - l)
                        l = hashmap[s[i]] + 1
                        # print(l, s[i], hashmap[s[i]], maxsubstring)
                    # in hashmap before the window
                    hashmap[s[i]] = i
            # print(hashmap)
        
        return max(maxsubstring, len(s) - l)