class Solution:
    def rle(self, s: str) -> str:
        i = 0
        count = 1
        string = []
        while i < len(s):
            temp = s[i]
            while i + 1 < len(s) and temp == s[i+1]:
                i += 1
                count += 1
            i += 1
            string.append(str(count))
            string.append(temp)
            count = 1
        return ''.join(string)

    def countAndSay(self, n: int) -> str:
        ini = "1"
        for i in range(1, n):
            newini = self.rle(ini)
            ini = newini
        return ini