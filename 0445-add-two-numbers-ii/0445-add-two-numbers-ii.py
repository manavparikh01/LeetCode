# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prev1
            prev1 = curr
            curr = temp
        prev2 = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
        head = curr = ListNode()
        carry = 0
        while prev1 and prev2:
            sumval = prev1.val + prev2.val + carry
            finval = sumval % 10
            carry = sumval // 10
            curr.next = ListNode(finval)
            curr = curr.next
            prev1 = prev1.next
            prev2 = prev2.next
        while prev1:
            sumval = prev1.val + carry
            finval = sumval % 10
            carry = sumval // 10
            curr.next = ListNode(finval)
            curr = curr.next
            prev1 = prev1.next
        while prev2:
            sumval = prev2.val + carry
            finval = sumval % 10
            carry = sumval // 10
            curr.next = ListNode(finval)
            curr = curr.next
            prev2 = prev2.next
        if carry != 0:
            curr.next = ListNode(carry)
            curr = curr.next
        prevf = None
        curr = head.next
        while curr:
            temp = curr.next
            curr.next = prevf
            prevf = curr
            curr = temp
        return prevf