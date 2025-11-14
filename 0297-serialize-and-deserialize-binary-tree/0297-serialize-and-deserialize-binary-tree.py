# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dp(node):
            if node == None:
                res.append("N")
                return None
            res.append(str(node.val))
            dp(node.left)
            dp(node.right)
        dp(root)
        return ",".join(res)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        string = data.split(",")
        self.i = 0
        def dp():
            if string[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(string[self.i]))
            self.i += 1
            node.left = dp()
            node.right = dp()
            return node
        return dp()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))