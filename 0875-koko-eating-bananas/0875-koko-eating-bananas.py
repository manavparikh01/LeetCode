class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        rescount = max(piles)
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for n in piles:
                hours += math.ceil(n/k)
            if hours <= h:
                rescount = min(rescount, k)
                r = k - 1
            else:
                 l = k + 1
        return rescount