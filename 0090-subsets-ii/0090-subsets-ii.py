class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.slist = []
        self.mainlist = [[]]
        def dfs(i):
            if i >= len(nums):
                if self.slist[:] not in self.mainlist:
                    self.mainlist.append(self.slist[:])
                return
            self.slist.append(nums[i])
            dfs(i+1)
            self.slist.pop()
            while (i+1 < len(nums) and nums[i] == nums[i+1]):
                i = i+1
            dfs(i+1)
        dfs(0)
        return self.mainlist