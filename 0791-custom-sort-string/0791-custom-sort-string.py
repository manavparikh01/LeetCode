class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict1 = defaultdict()
        dict2 = defaultdict(int)
        res = []
        total = []
        for ind, char in enumerate(order):
            dict1[char] = ind
        for char in s:
            if char in dict1:
                dict2[char] += 1
            else:
                res.append(char)
        for char in dict1:
            for i in range(dict2[char]):
                total.append(char)
        subs = "".join(total) + "".join(res)
        return subs