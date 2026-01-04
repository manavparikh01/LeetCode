# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        mid = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        node = TreeNode(slow.val)
        mid.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node