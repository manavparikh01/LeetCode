# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        curr = head
        prev = None
        while curr.next != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr