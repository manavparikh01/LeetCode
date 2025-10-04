# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        string = ""
        if not root:
            return string
        def dfs(node):
            nonlocal string
            if not node:
                return
            string += str(node.val)
            string += ","
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return string[0:-1]
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        arr = data.split(",")
        def dfs(arr, lower, upper):
            if not arr:
                return None
            if not lower <= int(arr[0]) <= upper:
                return None
            value = int(arr.pop(0))
            node = TreeNode(value)
            node.left = dfs(arr, lower, node.val)
            node.right = dfs(arr, node.val, upper)
            return node
        
        return dfs(arr, -float("inf"), float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans