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
        hashmap = {}
        def dfs(root):
            if root in hashmap:
                return hashmap[root]
            copy = Node(root.val)
            hashmap[root] = copy
            for nei in root.neighbors:
                temp = dfs(nei)
                copy.neighbors.append(temp)
            return copy
        
        return dfs(node) if node else None