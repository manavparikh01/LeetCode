class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] = 1 + hashmap[i]
        temp = set()
        height = 0
        res = []
        for i in s:
            if len(temp) == 0 and height == 0:
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    res.append(1)
                else:
                    height += 1
                    temp.add(i)
            else:
                height += 1
                hashmap[i] -= 1
                temp.add(i)
                if hashmap[i] == 0:
                    temp.remove(i)
                if len(temp) == 0:
                    res.append(height)
                    height = 0
        return res

