class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for conn in connections:
            adj[conn[0]].append(conn[1])
            adj[conn[1]].append(conn[0])
        visit = set()
        tim = [-1] * n 
        low = [-1] * n
        bridges = []

        def dfs(node, parent, time):
            visit.add(node)
            tim[node] = time
            low[node] = time

            for neigh in adj[node]:
                if neigh not in visit:
                    dfs(neigh, node, time + 1)
                    low[node] = min(low[node], low[neigh])

                    if low[neigh] > tim[node]:
                        bridges.append([node, neigh])
                elif neigh != parent:
                    low[node] = min(low[node], low[neigh])
            
        dfs(0, -1, 0)
        return bridges

