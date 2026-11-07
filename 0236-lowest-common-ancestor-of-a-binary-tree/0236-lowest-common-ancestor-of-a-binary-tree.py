# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inOrder(node):
            if node is None or node == p or node == q:
                return node
            left = inOrder(node.left)
            right = inOrder(node.right)
            if left and right:
                return node
            return left if left else right
        return inOrder(root)
        