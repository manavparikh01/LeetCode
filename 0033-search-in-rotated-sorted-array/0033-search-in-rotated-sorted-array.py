class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r)
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            elif nums[l] < nums[r]: # the array is sorted
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # the array is not sorted
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[l]: # the mid is in the left sorted array
                    if nums[mid] > target:
                        if nums[l] > target:
                            l = mid + 1
                        else:
                            r = mid - 1
                    else:
                        l = mid + 1
                else: # the mid is in the right sorted array
                    if nums[mid] < target:
                        if nums[r] < target:
                            r = mid - 1
                        else:
                            l = mid + 1
                    else:
                        r = mid - 1
        return -1