# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        l = 0
        r = len(nums)
        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[l:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:r])
        return node