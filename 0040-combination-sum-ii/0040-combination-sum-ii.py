class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # if sum(candidates) < target:
        #     return []
        slist = []
        mlist = []
        def dfs(ind, target):
            if ind >= len(candidates) or target < 0:
                if target == 0:
                    if slist not in mlist:
                        mlist.append(slist[:])
                    return
                return
            # if candidates[ind] <= target:
            slist.append(candidates[ind])
            dfs(ind + 1, target - candidates[ind])
            slist.pop()
            while (ind + 1 < len(candidates) and candidates[ind] == candidates[ind+1]):
                ind = ind + 1
            dfs(ind + 1, target)
            # dfs(ind + 1, target)
        dfs(0, target)
        return mlist