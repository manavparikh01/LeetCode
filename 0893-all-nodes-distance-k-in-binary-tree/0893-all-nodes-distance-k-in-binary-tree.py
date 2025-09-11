# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parentmap = {}
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parentmap[node.left] = node
                q.append(node.left)
            if node.right:
                parentmap[node.right] = node
                q.append(node.right)
        seen = {target}
        q = deque([target])
        dist = 0
        while q and dist < k:
            level_size = len(q)
            for _ in range(level_size):
                cur = q.popleft()
                for nei in (cur.left, cur.right, parentmap.get(cur)):
                    if nei and nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            dist += 1
        res = []
        while q:
            res.append(q.popleft().val)
        return res
        