"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            temp = None
            i = 0
            while i < length:
                node = queue.popleft()
                if i > 0:
                    temp.next = node
                temp = node
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                i += 1
            temp.next = None
        return root