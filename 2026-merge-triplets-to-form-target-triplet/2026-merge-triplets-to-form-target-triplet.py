class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indices = set()
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            for idx, v in enumerate(i):
                if v == target[idx]:
                    indices.add(idx)
        if len(indices) == 3:
            return True
        return False