# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorderlist = deque()
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            self.inorderlist.append(node)
            dfs(node.right)
        dfs(self.root)
        self.start = TreeNode()
        self.start.right = self.inorderlist[0]

    def next(self) -> int:
        temp = self.inorderlist.popleft()
        return temp.val

    def hasNext(self) -> bool:
        return True if len(self.inorderlist) > 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()