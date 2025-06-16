# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            lesres = []
            while size > 0:
                size -= 1
                temp = queue.popleft()
                lesres.append(temp.val)
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            res.append(lesres)
        return res