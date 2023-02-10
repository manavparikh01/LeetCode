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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
        {
            return head;
        }
        if (head.next == null)
        {
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        ListNode curr = head;
        ListNode prev = head;
        boolean count = false;
        curr = curr.next;
        // while (curr.next != null && curr.val == curr.next.val)
        // {
        //     curr = curr.next;
        //     count = true;
        //     //System.out.println(curr.val);
        // }
        // if (count)
        // {
        //     head = curr.next;
        // }
        // else
        // {
        //     head = curr;
        // }
        while (curr != null && curr.next != null)
        {
            if (curr.val == curr.next.val)
            {
                while (curr != null && curr.next != null && curr.val == curr.next.val)
                {
                    curr = curr.next;
                }
                prev.next = curr.next;
                curr = prev.next;
            }
            else
            {
                prev = curr;
                curr = curr.next;
            }
        }
        return head.next;
//         if(head == null || head.next == null){
//             return head;
//         }

//         ListNode dummy = new ListNode(0);
//         dummy.next = head;
//         head = dummy;

//         while (head.next != null && head.next.next != null) {
//             if (head.next.val == head.next.next.val) {
//                 int val = head.next.val;
//                 while (head.next != null && head.next.val == val) {
//                     head.next = head.next.next;
//                 }            
//             } else {
//                 head = head.next;
//             }
//         }

//         return dummy.next;
    }
}