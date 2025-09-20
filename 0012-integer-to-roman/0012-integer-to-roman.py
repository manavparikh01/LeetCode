class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        length = len(str(num)) - 1
        res = ""
        while length >= 0:
            div = 10**length
            digit = num // div
            if digit == 1 or digit == 5:
                res += hashmap[digit*div]
            elif digit == 4:
                res += hashmap[1*div]
                res += hashmap[5*div]
            elif digit == 9:
                res += hashmap[1*div]
                res += hashmap[10*div]
            else:
                if digit < 5:
                    while digit > 0:
                        res += hashmap[1*div]
                        digit -= 1
                else:
                    res += hashmap[5*div]
                    digit -= 5
                    while digit > 0:
                        res += hashmap[1*div]
                        digit -= 1
            num = num % 10**length
            length -= 1
        return res
           

