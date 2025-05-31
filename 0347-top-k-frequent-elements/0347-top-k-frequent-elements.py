class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        res = [[] for i in range(len(nums) + 1)]
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        for n, c in dic.items():
            res[c].append(n)
        fin = []
        for i in range(len(res) - 1, 0, -1):
            for n in res[i]:
                fin.append(n)
                if len(fin) == k:
                    return fin
