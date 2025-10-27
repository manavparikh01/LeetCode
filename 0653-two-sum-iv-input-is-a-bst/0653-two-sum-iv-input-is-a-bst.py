# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        order = set()
        def dp(node):
            if node == None:
                return False
            if k - node.val in order:
                return True
            order.add(node.val)
            return dp(node.left) or dp(node.right)
        return dp(root)