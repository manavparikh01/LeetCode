class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number * 10 + i
        number += 1
        res = []
        while number > 0:
            digit = number % 10
            res.append(digit)
            number //= 10
        return res[::-1]