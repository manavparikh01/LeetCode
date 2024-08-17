# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        mainprev = dummy
        
        while True:
            kth = self.getKth(mainprev, k)
            if not kth:
                break
            groupkth = kth.next
            prev = kth.next
            curr = mainprev.next
            while curr != groupkth:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = mainprev.next
            mainprev.next = kth
            mainprev = temp
        return dummy.next
            
        
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
            