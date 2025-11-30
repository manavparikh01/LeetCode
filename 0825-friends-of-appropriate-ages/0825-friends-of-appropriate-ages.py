class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        hashmap = defaultdict(int)
        agesset = []
        ages.sort()
        for age in ages:
            hashmap[age] += 1
            if age not in agesset:
                agesset.append(age)
        res = 0
        for i in range(0, len(agesset)):
            eon = (0.5 * agesset[i]) + 7
            sim = hashmap[agesset[i]]
            for j in range(i, -1, -1):
                if agesset[j] <= eon:
                    break
                res += sim * hashmap[agesset[j]]
                if i == j:
                    res -= sim
        return res