# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        curr = head
        while curr:
            s = s + str(curr.val)
            curr = curr.next
        if s == s[::-1]:
            return True
        return False