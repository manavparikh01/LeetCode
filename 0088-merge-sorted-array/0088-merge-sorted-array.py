class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         for i in range(0, n, 1):
#             nums1[m+i] = nums2[i]
        
#         nums1.sort()

        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                nums2.sort()
        for i in range(n):
            nums1[i+m] = nums2[i]
        