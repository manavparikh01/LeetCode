class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        heapletter = [] #minheap
        arraydigit = []
        for log in logs:
            split = log.split()
            if split[1].isdigit():
                arraydigit.append(log)
                continue
            split1 = log.split(" ", 1)
            heapq.heappush(heapletter, [split1[1], split1[0]])
        res = []
        while heapletter:
            s1, s0 = heapq.heappop(heapletter)
            res.append(s0 + " " + s1)
        for arr in arraydigit:
            res.append(arr)
        return res