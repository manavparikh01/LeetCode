# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(nodel, noder):
            if nodel == None and noder == None:
                return True
            if nodel == None and noder != None:
                return False
            if nodel != None and noder == None:
                return False
            if nodel.val != noder.val:
                return False
            
            one = dfs(nodel.left, noder.right)
            two = dfs(nodel.right, noder.left)
            return one == two == True

        return dfs(root.left, root.right)
