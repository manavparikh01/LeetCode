class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        # hashmap = {}
        # visited = set()
        # res = []

        # for depends in prerequisites:
        #     if depends[0] in hashmap:
        #         hashmap[depends[0]].append(depends[1])
        #     else:
        #         hashmap[depends[0]] = [depends[1]]
    
        
        # def ifPossible(i):
        #     if i not in hashmap:
        #         if i not in res:
        #             res.append(i)
        #         return True
        #     if i in visited:
        #         return False
        #     visited.add(i)
        #     for idx in hashmap[i]:
        #         if ifPossible(idx) == False:
        #             return False
        #     visited.remove(i)
        #     if i not in res:
        #         res.append(i)
        #     return True

        # for i in range(numCourses):
        #     if ifPossible(i) == False:
        #         return []
                
        # return res