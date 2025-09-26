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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        queue = deque()
        curr = root
        queue.append(curr)
        while queue:
            length = len(queue)
            temp = None
            for i in range(length):
                node = queue.popleft()
                if i > 0:
                    temp.next = node
                temp = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            temp.next = None
        return root