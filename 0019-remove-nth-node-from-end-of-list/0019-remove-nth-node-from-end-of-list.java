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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        if (head == null)
        {
            return head;
        }
        for (int i=0;i<n;i++)
        {
            if (curr == null)
            {
                return curr;
            }
            curr = curr.next;
        }
        if (curr == null)
        {
            return head.next;
        }
        ListNode first = head;
        while (curr.next != null)
        {
            first = first.next;
            curr = curr.next;
        }
        first.next = first.next.next;
        return head;
    }
}