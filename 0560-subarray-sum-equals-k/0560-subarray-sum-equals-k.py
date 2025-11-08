class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr = [0] * len(nums)
        sumone = 0
        for i in range(len(nums)):
            sumone += nums[i]
            arr[i] = sumone
        #print(arr)
        pre = defaultdict(int)
        res = 0
        for i in range(len(arr)):
            #print(pre, arr[i], arr[i] - k)
            if arr[i] == k:
                res += 1
            if arr[i] - k in pre:
                res += pre[arr[i] - k]
            pre[arr[i]] += 1
            #print(res)
        return res