class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i, val in enumerate(equations):
            a, b = val
            adjList[a].append([b, values[i]])
            adjList[b].append([a, 1/values[i]])
        def bfs(src, dest):
            if src not in adjList or dest not in adjList:
                return -1
            queue = deque()
            visit = set()
            queue.append([src, 1])
            visit.add(src)
            while queue:
                s, w = queue.popleft()
                if s == dest:
                    return w
                for neigh, weight in adjList[s]:
                    if neigh not in visit:
                        queue.append([neigh, weight * w])
                        visit.add(neigh)
            return -1

        res = []
        for que in queries:
            res.append(bfs(que[0], que[1]))
        
        return res