# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None and n == 1:
            return None
        l = 0
        curr = head
        curr2 = head
        while curr != None:
            l = l+1
            curr = curr.next
        if l == n:
            return head.next
        i = l - n
        while i > 1:
            head = head.next
            i = i - 1
        head.next = head.next.next
        return curr2