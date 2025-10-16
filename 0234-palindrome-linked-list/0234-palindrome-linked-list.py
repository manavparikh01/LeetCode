# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = dcurr = head
        while dcurr.next and dcurr.next.next:
            curr = curr.next
            dcurr = dcurr.next.next
        prev = None
        ncurr = curr.next
        while ncurr:
            temp = ncurr.next
            ncurr.next = prev
            prev = ncurr
            ncurr = temp
        mcurr = head
        while mcurr and prev:
            if mcurr.val != prev.val:
                return False
            mcurr = mcurr.next
            prev = prev.next
        return True