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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
        {
            return null;
        }
        if (lists == null)
        {
            return null;
        }
        ArrayList<Integer> al = new ArrayList<Integer>();
        for (int i = 0;i<lists.length;i++)
        {
            ListNode curr = lists[i];
            while (curr != null)
            {
                al.add(curr.val);
                curr = curr.next;
            }
        }
        if (al.size() == 0)
        {
            return null;
        }
        Collections.sort(al);
        ListNode head = new ListNode(al.get(0));
        ListNode curr = head;
        for (int i = 1;i<al.size();i++)
        {
            ListNode newHead = new ListNode(al.get(i));
            curr.next = newHead;
            curr = newHead;
        }
        return head;
    }
}