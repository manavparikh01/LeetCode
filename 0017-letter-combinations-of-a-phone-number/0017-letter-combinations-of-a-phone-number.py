class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        string = ""
        num = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        def dp(i):
            nonlocal string, res, num
            if len(string) == len(digits):
                temp = string
                res.append(temp)
                return
            for j in range(len(num[int(digits[i])])):
                string += num[int(digits[i])][j]
                dp(i + 1)
                string = string[:-1]
            return
        dp(0)
        return res