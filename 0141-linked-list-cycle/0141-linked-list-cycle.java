/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null)
        {
            return false;
        }
        ListNode curr = head;
        ListNode curr1 = head;
        while (curr1.next != null && curr1.next.next != null && curr.next != null)
        {
            curr = curr.next;
            curr1 = curr1.next.next;
            if (curr == curr1)
            {
                return true;
            }
        }
        return false;
    }
}