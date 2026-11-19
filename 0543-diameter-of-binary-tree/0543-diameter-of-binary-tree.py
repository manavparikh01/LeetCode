# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            left_side = dfs(root.left)
            right_side = dfs(root.right)
            total = left_side + right_side
            res = max(res, total)
            return max(1 + left_side, 1 + right_side)
        dfs(root)
        return res
