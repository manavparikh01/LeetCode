# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

        # if root == None:
        #     return None
        # def dfs(node):
        #     if node == None:
        #         return None
        #     if node == p or node == q:
        #         return node
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if left and right:
        #         return node
        #     return left if left else right
        # return dfs(root)    