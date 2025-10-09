class Solution:
    def myAtoi(self, s: str) -> int:
        isMinus = False
        isPlus = False
        didnumchange = False
        num = 0
        i = 0
        LAR = 2147483647
        LOW = -2147483648
        for i in range(len(s)):
            if not s[i].isdigit():
                if didnumchange or isMinus or isPlus:
                    break
                else:
                    if s[i] == "-":
                        isMinus = True
                    elif s[i] == "+":
                        isPlus = True
                    elif s[i] == " ":
                        continue
                    else:
                        break
            else:
                didnumchange = True
                num = num * 10 + int(s[i])
        finnum = num if isMinus == False else -num
        if finnum > LAR:
            return LAR
        if finnum < LOW:
            return LOW
        return finnum