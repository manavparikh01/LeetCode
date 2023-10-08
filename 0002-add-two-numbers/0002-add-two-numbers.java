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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null)
        {
            return null;
        }
        if (l1 == null)
        {
            return l2;
        }
        if (l2 == null)
        {
            return l1;
        }
        ListNode curr = l1;
        ListNode curr1 = l2;
        int valu = curr.val + curr1.val;
        ListNode curr2 = new ListNode(valu%10);
        ListNode curr3 = curr2;
        curr = curr.next;
        curr1 = curr1.next;
        while (curr != null && curr1 != null)
        {
            valu = curr.val + curr1.val + valu/10;
            ListNode newNod = new ListNode(valu%10);
            curr2.next = newNod;
            curr = curr.next;
            curr1 = curr1.next;
            curr2 = curr2.next;
        }
        while (curr != null)
        {
            valu = curr.val + valu/10;
            ListNode newNod = new ListNode(valu%10);
            curr2.next = newNod;
            curr = curr.next;
            curr2 = curr2.next;
        }
        while (curr1 != null)
        {
            valu = curr1.val + valu/10;
            ListNode newNod = new ListNode(valu%10);
            curr2.next = newNod;
            curr1 = curr1.next;
            curr2 = curr2.next;
        }
        if (valu > 9)
        {
            valu = valu/10;
            ListNode newNod = new ListNode(valu);
            curr2.next = newNod;
            curr2 = curr2.next;
        }
        return curr3;
    }
}