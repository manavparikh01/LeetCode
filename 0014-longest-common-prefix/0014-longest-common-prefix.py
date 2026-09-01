class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        count = 0
        while i < len(strs[0]):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:count]
            count += 1
            i += 1
        return strs[0][:count]