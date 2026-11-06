# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        reslist = []
        while queue:
            templist = []
            for i in range(len(queue)):
                tnode = queue.popleft()
                templist.append(tnode.val)
                if tnode.left != None:
                    queue.append(tnode.left)
                if tnode.right != None:
                    queue.append(tnode.right)
            reslist.append(templist)
        return reslist