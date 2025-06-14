# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        curr = head
        currfast = head.next
        while currfast and currfast.next and currfast.next.next:
            if curr == currfast:
                return True
            currfast = currfast.next.next
            curr = curr.next
        return False