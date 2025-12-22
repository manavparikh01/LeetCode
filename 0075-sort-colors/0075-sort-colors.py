class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        res = []
        ind = 0
        for i in range(3):
            length = 0
            if i in hashMap:
                length = hashMap[i]
            for j in range(length):
                nums[ind] = i
                ind += 1