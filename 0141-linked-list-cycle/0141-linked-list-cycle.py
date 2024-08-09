# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        listofnodes = []
        curr = head
        while curr != None:
            if curr in listofnodes:
                return True
            listofnodes.append(curr)
            curr = curr.next
        return False