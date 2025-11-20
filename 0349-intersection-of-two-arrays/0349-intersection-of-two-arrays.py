class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin = set()
        num1 = set()
        for num in nums1:
            num1.add(num)
        for num in nums2:
            if num not in fin and num in num1:
                fin.add(num)
        return list(fin)