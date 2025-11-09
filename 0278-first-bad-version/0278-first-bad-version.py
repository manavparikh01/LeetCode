# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == True:
                if mid == 1:
                    return 1
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1