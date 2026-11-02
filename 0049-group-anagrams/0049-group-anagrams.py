class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            sortstr = ''.join(sorted(i))
            hashmap[sortstr].append(i)
        finlist = []
        for k, value in hashmap.items():
            finlist.append(value)
        return finlist