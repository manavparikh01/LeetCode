class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        uniquehash = {}
        values = []
        for i in strs:
            ascilist = [0] * 128
            for characters in i:
                ascilist[ord(characters)] = ascilist[ord(characters)] + 1
            ascituple = tuple(ascilist)
            if ascituple not in uniquehash:
                uniquehash[ascituple] = [i]
            else:
                uniquehash[ascituple].append(i)
        for value in uniquehash.values():
            values.append(value)
        return values