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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null)
        {
            return head;
        }
        int i=1;
        ListNode curr = head;
        ListNode os = null;
        ListNode oe = null;
        ListNode es = null;
        ListNode ee = null;
        // curr = curr.next.next;
        while (curr != null)
        {
            if (i % 2 != 0)
            {
                if (os == null)
                {
                    os = curr;
                    oe = curr;
                    curr = curr.next;
                    i++;
                }
                else
                {
                    oe.next = curr;
                oe = curr;
                curr = curr.next;
                i++;
                }
            }
            else
            {
                if (es == null)
                {
                    es = curr;
                    ee = curr;
                    curr = curr.next;
                    i++;
                }
                else
                {
                    ee.next = curr;
                ee = curr;
                curr = curr.next;
                i++;
                }
            }
        }
        if (os == null || es == null)
        {
            return head;
        }
        oe.next = es;
        ee.next = null;
        return os;
    }
}