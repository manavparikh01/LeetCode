class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        temp = [False] * (len(s) + 1)
        temp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i:i+len(w)] == w:
                    temp[i] = temp[i + len(w)]
                if temp[i] == True:
                    break
            print(temp)
        return temp[0]