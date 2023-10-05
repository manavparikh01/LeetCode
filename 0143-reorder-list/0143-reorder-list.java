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
    public ListNode findTail(ListNode tail)
    {
        while (tail.next.next != null)
        {
            tail = tail.next;
        }
        ListNode last = tail.next;
        tail.next = null;
        //System.out.println(tail.val + " tail");
        return last;
    }
    public void reorderList(ListNode head) {
        if (head == null && head.next == null)
        {
            return;
        }
        ListNode curr = head;
        while (curr.next != null && curr.next.next != null)
        {
            ListNode tail = findTail(head);
            tail.next = curr.next;
            curr.next = tail;
            curr = tail.next;
            //System.out.println(curr.val);
        }
    }
}