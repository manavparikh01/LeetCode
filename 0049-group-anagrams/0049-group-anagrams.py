class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        output = []
        for st in strs:
            sorted_list = sorted(st)
            sorted_str = "".join(sorted_list)
            if sorted_str in hashmap:
                hashmap[sorted_str].append(st)
            else:
                hashmap[sorted_str] = [st]
        for key in hashmap:
            output.append(hashmap[key])
        return output