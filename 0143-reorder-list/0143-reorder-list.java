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
    public void reorderList(ListNode head) {
        if (head == null && (head.next == null || head.next.next == null))
        {
            return;
        }
        ListNode curr = head;
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode rev = slow.next;
        slow.next = null;
        //System.out.println(rev.val);
        ListNode prev = null;
        while (rev != null)
        {
            ListNode next = rev.next;
            rev.next = prev;
            prev = rev;
            rev = next;
        }
        //System.out.println(prev.val + " " + prev.next.val);
        while (prev != null)
        {
            ListNode temp = prev.next;
            prev.next = curr.next;
            //System.out.println(curr.next.val + "h");
            curr.next = prev;
            curr = prev.next;
            prev = temp;
            //System.out.println(prev.val);
        }
    }
}