# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        prev = None
        while curr.next != None:
            temp = curr.next.val
            curr.next.val = curr.val
            curr.val = temp
            prev = curr
            curr = curr.next
        prev.next = None
        
        
            