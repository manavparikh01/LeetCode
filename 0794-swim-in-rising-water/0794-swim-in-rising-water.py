class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        visit.add((0, 0))
        minheap = [[grid[0][0], 0, 0]]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while minheap:
            time, r, c = heapq.heappop(minheap)
            if r == n-1 and c == n-1:
                return time
            for x, y in directions:
                nr, nc = r+x, c+y
                if (nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in visit):
                    continue
                print(nr, nc)
                visit.add((nr, nc))
                heapq.heappush(minheap, [max(time, grid[nr][nc]), nr, nc])

        