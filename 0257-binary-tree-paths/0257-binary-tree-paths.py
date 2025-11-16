# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(arr, node):
            nonlocal res
            if node == None:
                return
            arr.append(str(node.val))
            dfs(arr, node.left)
            dfs(arr, node.right)
            if node.left == None and node.right == None:
                res.append(arr.copy())
            arr.pop()
        dfs([], root)
        final = []
        for re in res:
            string = "->".join(re)
            final.append(string)
        return final