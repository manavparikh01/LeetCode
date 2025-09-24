# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque()
        queue.append(root)
        i = 0
        res = []
        while queue:
            length = len(queue)
            temp = []
            for j in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if i % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            i += 1
        return res
