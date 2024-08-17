# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict = {}
        curr = head
        i = 0
        while curr:
            if curr not in dict:
                dict[curr] = i
                curr = curr.next
            else:
                return curr
            i += 1
        return None
        