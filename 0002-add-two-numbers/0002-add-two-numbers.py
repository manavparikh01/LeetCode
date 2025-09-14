# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sumnode = dummy
        extra = 0
        while l1 and l2:
            tempsum = l1.val + l2.val
            tempsum += extra
            finsum = tempsum % 10
            extra = tempsum // 10
            curr = ListNode(finsum)
            sumnode.next = curr
            sumnode = sumnode.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            tempsum = l1.val
            tempsum += extra
            finsum = tempsum % 10
            extra = tempsum // 10
            curr = ListNode(finsum)
            sumnode.next = curr
            sumnode = sumnode.next
            l1 = l1.next
        while l2:
            tempsum = l2.val
            tempsum += extra
            finsum = tempsum % 10
            extra = tempsum // 10
            curr = ListNode(finsum)
            sumnode.next = curr
            sumnode = sumnode.next
            l2 = l2.next
        if extra != 0:
            curr = ListNode(extra)
            sumnode.next = curr
            sumnode = sumnode.next
        return dummy.next