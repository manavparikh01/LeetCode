/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
        {
            return list2;
        }
        if (list2 == null)
        {
            return list1;
        }
        ListNode ls1 = list1;
        ListNode ls2 = list2;
        ListNode head = null;
        ListNode tail = null;
        if (ls1.val <= ls2.val)
        {
            head = ls1;
            tail = ls1;
            ls1 = ls1.next;
        }
        else
        {
            head = ls2;
            tail = ls2;
            ls2 = ls2.next;
        }
        while (ls1 != null && ls2 != null)
        {
            if (ls1.val <= ls2.val)
            {
                tail.next = ls1;
                tail = ls1;
                ls1 = ls1.next;
            }
            else
            {
                tail.next = ls2;
                tail = ls2;
                ls2 = ls2.next;
            }
        }
        if (ls1 == null)
        {
            tail.next = ls2;
        }
        else
        {
            tail.next = ls1;
        }
        return head;
    }
}