# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return True
        curr = head
        curr2 = head
        curr3 = head
        while curr2.next != None and curr2.next.next != None:
            curr = curr.next
            curr2 = curr2.next.next
        prev = None
        curr4 = curr.next
        while curr4:
            temp = curr4.next
            curr4.next = prev
            prev = curr4
            curr4 = temp
        #print(prev.val, curr3.val)
        while prev:
            #print(prev.val, curr3.val, "Hello")
            if curr3.val != prev.val:
                return False
            curr3 = curr3.next
            prev = prev.next
        return True
            