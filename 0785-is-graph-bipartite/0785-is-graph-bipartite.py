class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        arr = [0] * len(graph)
        def dp(i):
            if arr[i]:
                return True
            q = deque()
            q.append(i)
            arr[i] = -1
            while q:
                n = q.popleft()
                for neigh in graph[n]:
                    if arr[n] == arr[neigh]:
                        return False
                    elif not arr[neigh]:
                        q.append(neigh)
                        arr[neigh] = -1 * arr[n]
            return True
        
        for i in range(len(graph)):
            if not dp(i):
                return False
        
        return True