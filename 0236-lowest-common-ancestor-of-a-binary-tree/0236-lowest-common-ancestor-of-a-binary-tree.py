# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        isFound = False
        def dp(node):
            nonlocal res, isFound
            if node == None or isFound == True:
                return False
            left = dp(node.left)
            middle = True if node == p or node == q else False
            right = dp(node.right)
            if ((left and middle) or (middle and right) or (left and right)) and isFound == False:
                res = node
                isFound = True
            return (left or middle or right)
        dp(root)
        return res
        