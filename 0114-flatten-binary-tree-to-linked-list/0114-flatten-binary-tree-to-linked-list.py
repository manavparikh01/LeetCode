# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def pre(node):
            if node is None:
                return
            res.append(node)
            pre(node.left)
            pre(node.right)
            return
        pre(root)
        prev = TreeNode(-101)
        for node in res:
            prev.right = node
            node.left = None
            prev = node
        return root


            