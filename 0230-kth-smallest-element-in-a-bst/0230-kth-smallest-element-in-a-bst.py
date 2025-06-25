# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        res = root.val
        def dfs(node):
            nonlocal n, res
            if node == None:
                return 
            dfs(node.left)
            n += 1
            if n == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
        