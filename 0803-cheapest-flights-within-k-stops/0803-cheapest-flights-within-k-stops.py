class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pricelist = [float('inf')] * n
        pricelist[src] = 0
        for i in range(k + 1):
            temppricelist = pricelist.copy()
            for s, d, p in flights:
                if pricelist[s] == float('inf'):
                    continue
                if pricelist[s] + p < temppricelist[d]:
                    temppricelist[d] = pricelist[s] + p
            pricelist = temppricelist
        return -1 if pricelist[dst] == float('inf') else pricelist[dst]
        
