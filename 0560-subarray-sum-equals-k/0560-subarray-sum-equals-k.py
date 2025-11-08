class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumone = 0
        #print(arr)
        pre = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            #print(pre, arr[i], arr[i] - k)
            sumone += nums[i]
            if sumone == k:
                res += 1
            if sumone - k in pre:
                res += pre[sumone - k]
            pre[sumone] += 1
            #print(res)
        return res