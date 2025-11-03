class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = nums.copy()
        for i in range(len(nums) - 1, -1, -1):
            temp = []
            while stack and stack[-1] <= nums[i]:
                temp.append(stack.pop())
            if stack:
                if stack[-1] > nums[i]:
                    arr[i] = stack[-1]
            while temp:
                stack.append(temp.pop())
            stack.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if arr[i] != nums[i]:
                continue
            temp = []
            while stack and stack[-1] <= nums[i]:
                temp.append(stack.pop())
            if stack:
                if stack[-1] > nums[i]:
                    arr[i] = stack[-1]
            else:
                arr[i] = -1
            while temp:
                stack.append(temp.pop())
            stack.append(nums[i])
        return arr