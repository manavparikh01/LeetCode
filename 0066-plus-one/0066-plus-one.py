class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]     
        # number = 0
        # for i in digits:
        #     number = number * 10 + i
        # number += 1
        # res = []
        # while number > 0:
        #     digit = number % 10
        #     res.append(digit)
        #     number //= 10
        # return res[::-1]