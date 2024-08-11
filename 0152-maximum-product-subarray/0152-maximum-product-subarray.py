class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmin = 1
        currmax = 1
        for i in nums:
            if i == 0:
                currmax = 1
                currmin = 1
            else:
                tempmax = currmax
                currmax = max(currmax * i, currmin * i, i)
                currmin = min(tempmax * i, currmin * i, i)
                #print(currmax, currmin, i)
                res = max(currmax, currmin, res)
        return res