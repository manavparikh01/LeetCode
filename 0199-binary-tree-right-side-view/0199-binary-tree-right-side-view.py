# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            for i in range(len(queue)):
                tnode = queue.popleft()
                if tnode.left:
                    queue.append(tnode.left)
                if tnode.right:
                    queue.append(tnode.right)
                if i == length - 1:
                    res.append(tnode.val)
        return res
