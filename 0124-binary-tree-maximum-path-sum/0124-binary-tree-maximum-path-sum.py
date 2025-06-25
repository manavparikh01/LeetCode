# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if root == None:
                return float("-inf")
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right+root.val, root.val, left, right)
            return max(left + root.val, right + root.val, root.val)
        val = dfs(root)
        res = max(res, val)
        return res