class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        val_ones = { 0: "Zero",
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty"}
        val_tens = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        val_others = {100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }
        def getstring(s):
            res = []
            hun = s // 100
            if hun:
                res.append(val_ones[hun] + " Hundred")
            tens = s % 100
            if tens >= 20:
                tens_ones = tens // 10
                res.append(val_tens[tens_ones * 10])
                ones = tens % 10
                if ones:
                    res.append(val_ones[ones])
            elif tens:
                res.append(val_ones[tens])
            return " ".join(res)

        addons = ["", " Thousand", " Million", " Billion"]
        addonsi = 0
        res = []
        while num > 0:
            nums = num % 1000
            s = getstring(nums)
            if s:
                res.append(s + addons[addonsi])
            num = num // 1000
            addonsi += 1
        res.reverse()
        return " ".join(res)

