# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        curr = list1
        curr2 = list2
        if curr.val <= curr2.val:
            temp = curr
            head = temp
            curr = curr.next
        else:
            temp = curr2
            head = temp
            curr2 = curr2.next
        while curr != None and curr2 != None:
            if curr.val <= curr2.val:
                temp.next = curr
                temp = curr
                curr = curr.next
            else:
                temp.next = curr2
                temp = curr2
                curr2 = curr2.next
        if curr != None:
            temp.next = curr
        if curr2 != None:
            temp.next = curr2
        return head