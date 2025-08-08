class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(len(points))}
        for i in range(0, len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                hashmap[i].append([distance, j])
                hashmap[j].append([distance, i])
        
        res = 0
        minlist = [[0,0]]
        visit = set()
        while minlist:
            distance, index = heapq.heappop(minlist)
            if index in visit:
                continue
            visit.add(index)
            res += distance
            for dis, ind in hashmap[index]:
                if ind not in visit:
                    heapq.heappush(minlist, [dis, ind])
        return res
