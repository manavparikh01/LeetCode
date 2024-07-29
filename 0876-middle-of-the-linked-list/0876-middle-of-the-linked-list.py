# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        currone = head
        while curr != None and curr.next != None:
            currone = currone.next
            curr = curr.next.next
        return currone
            