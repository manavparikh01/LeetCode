class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        hashmap = {}
        start = 0 # start time
        last = 1 # 1 for start and 0 for end
        prev = -1 # for last executed function
        stack = []
        for log in logs:
            f, func, t = log.split(":")
            #print(f, func, t)
            fint = int(f)
            if f not in hashmap:
                diff = int(t) - start
                if stack:
                    hashmap[stack[-1]] += diff
                hashmap[f] = 0
                start = int(t)
                last = 1
                stack.append(f)
            else:
                if func == "start":
                    diff = int(t) - start
                    if stack:
                        hashmap[stack[-1]] += diff
                    start = int(t)
                    last = 1
                    stack.append(f)
                else:
                    diff = int(t) + 1 - start
                    hashmap[f] += diff
                    start = int(t) + 1
                    last = 0
                    stack.pop()
            #print(hashmap)
        res = []
        for i in range(n):
            res.append(hashmap[str(i)])
        return res