# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr = head
        tail = head
        newcurr = head
        height = 1
        while tail.next != None:
            tail = tail.next
            height += 1
        # reverse from half point
        half = (height + 1) // 2
        while half > 1:
            curr = curr.next
            half -= 1
        #print(curr.val)
        curr1 = curr.next
        curr.next = None
        prev = None
        while curr1:
            temp = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = temp
        # join these two linked lists
        while newcurr and prev:
            print(newcurr.val, prev.val)
            temp = newcurr.next
            newcurr.next = prev
            tempnew = prev.next
            prev.next = temp
            newcurr = temp
            prev = tempnew
        return head
        
        