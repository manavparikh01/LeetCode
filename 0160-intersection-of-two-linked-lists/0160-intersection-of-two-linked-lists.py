# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listofnodes = []
        curr = headA
        while curr != None:
            listofnodes.append(curr)
            curr = curr.next
        curr2 = headB
        while curr2 != None:
            if curr2 in listofnodes:
                return curr2
            curr2 = curr2.next
        return None