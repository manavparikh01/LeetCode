class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        def rob1():
            arr = [0] * (len(nums) - 1)
            arr[0] = nums[0]
            arr[1] = max(arr[0], nums[1])
            for i in range(2, len(nums) - 1):
                arr[i] = max(arr[i-1], arr[i-2] + nums[i])
            return arr[-1]
        def rob2():
            arr = [0] * (len(nums) - 1)
            arr[0] = nums[1]
            arr[1] = max(arr[0], nums[2])
            for i in range(3, len(nums)):
                arr[i-1] = max(arr[i-2], arr[i-3] + nums[i])
            return arr[-1]
        return max(rob1(), rob2())