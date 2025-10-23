"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        adj = defaultdict()
        def dp(root):
            if root in adj:
                return adj[root]
            newnode = Node(root.val)
            adj[root] = newnode
            for neig in root.neighbors:
                newnode.neighbors.append(dp(neig))
            return newnode
        return dp(node)
        