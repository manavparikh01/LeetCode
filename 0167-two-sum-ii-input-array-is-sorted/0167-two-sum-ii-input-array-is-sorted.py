class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        # hashmap = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in hashmap:
        #         return [hashmap[target - numbers[i]] + 1, i + 1]
        #     hashmap[numbers[i]] = i
        