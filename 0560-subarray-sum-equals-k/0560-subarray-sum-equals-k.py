class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1, 2, 3]
        # [1, 3, 6]
        hashmap = defaultdict(int)
        lnums = [0] * len(nums)
        lnums[0] = nums[0]
        rescount = 0
        for i in range(1, len(nums)):
            lnums[i] = lnums[i - 1] + nums[i]
        # print(lnums)
        for num in lnums:
            # print(setlist, num - k, num)
            if num == k:
                rescount += 1
            if num - k in hashmap:
                rescount += hashmap[num - k]
            hashmap[num] += 1
        return rescount