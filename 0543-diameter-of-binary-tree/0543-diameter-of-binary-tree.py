# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        dia = 0
        def dfs(node):
            nonlocal dia
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            dia = max(dia, left + right)
            return 1 + max(left, right)
        dfs(root)
        return dia