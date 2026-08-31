class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        ele = float("-inf")
        for n in nums:
            if counter == 0:
                ele = n
                counter += 1
            else:
                if ele == n:
                    counter += 1
                else:
                    counter -= 1
        return ele

