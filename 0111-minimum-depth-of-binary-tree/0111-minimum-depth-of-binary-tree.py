# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # total = 0
        res = float("inf")
        def dfs(node, total):
            nonlocal res
            if node == None:
                return
            if node.left == None and node.right == None:
                res = min(res, total)
                return
            dfs(node.left, total + 1)
            dfs(node.right, total + 1)
            return
        dfs(root, 1)
        return res