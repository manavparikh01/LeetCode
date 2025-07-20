class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        isPossible = set()
        notPossible = set()
        visited = set()
        for depends in prerequisites:
            if depends[0] in hashmap:
                hashmap[depends[0]].append(depends[1])
            else:
                hashmap[depends[0]] = [depends[1]]

        def ifPossible(i):
            if i not in hashmap or i in isPossible:
                return True
            if i in notPossible or i in visited:
                return False
            visited.add(i)
            for idx in hashmap[i]:
                if ifPossible(idx) == False:
                    notPossible.add(i)
                    return False
            visited.remove(i)
            isPossible.add(i)
            return True
        
        for i in range(numCourses):
            if ifPossible(i) == False:
                return False
        
        return True