# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = -1
        self.i = 1
        def dfs(root):
            nonlocal res
            if root is None or self.i > k:
                return
            dfs(root.left)
            if self.i == k:
                res = root.val
            self.i += 1
            dfs(root.right)
            return
        dfs(root)
        return res