class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l+h)//2
            print(mid)
            if (mid - 0 + 1) % 2 == 1:
                if mid - 1 >=0 and nums[mid - 1] == nums[mid]:
                    h = mid - 1
                    print(h, "helo 1")
                elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                    l = mid + 1
                    print(l, "helo 2")
                else:
                    return nums[mid]
            else:
                if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                    l = mid + 1
                    print(l, "helo 3")
                elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                    h = mid - 1
                    print(h, "helo 4")
                else:
                    return nums[mid]
        return -1
            