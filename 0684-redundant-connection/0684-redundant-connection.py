class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num = len(edges)
        parent = [i for i in range(num + 1)]
        rank = [1] * (num + 1)

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)
            if parent1 == parent2:
                return False
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]