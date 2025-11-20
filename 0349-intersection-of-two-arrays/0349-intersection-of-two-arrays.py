class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin = []
        for num in nums2:
            if num not in fin and num in nums1:
                fin.append(num)
        return fin