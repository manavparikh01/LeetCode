# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(root, subRoot):
        if root == None and subRoot == None:
            return True
        if (root == None and subRoot != None) or (root != None and subRoot == None) or root.val != subRoot.val:
            return False
        return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)