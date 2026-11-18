class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        hashdict = {}
        tset = set()
        yset = set()
        for listi in prerequisites:
            if listi[0] == listi[1]:
                return False
            if listi[0] not in hashdict:
                hashdict[listi[0]] = [listi[1]]
            else:
                hashdict[listi[0]].append(listi[1])

        def dfs(key):
            if key not in hashdict:
                yset.add(key)
                return True
            if key in yset:
                return True
            if key in tset:
                return False
            tset.add(key)
            for val in hashdict[key]:
                if dfs(val) == False:
                    return False
                yset.add(val)
            tset.remove(key)
            yset.add(key)
            return True

        for key in hashdict:
            if dfs(key) == False:
                return False
        
        return True

        