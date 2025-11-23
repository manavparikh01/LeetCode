class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = defaultdict(int)
        for num in nums1:
            n1[num] += 1
        res = []
        for num in nums2:
            if num in n1:
                res.append(num)
                n1[num] -= 1
                if n1[num] == 0:
                    del n1[num]
        return res