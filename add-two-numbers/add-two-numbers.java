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
        ListNode dummy=new ListNode(-1);
            ListNode curr=dummy;
            int carry=0;

        while(l1!=null&&l2!=null){
                int y=l1.val+l2.val+carry;
                carry=0;
                if(y>=10){

                        carry=y/10;
                        y=y%10;
                }
                ListNode node=new ListNode(y);
                curr.next=node;
                curr=curr.next;
                l1=l1.next;
                l2=l2.next;
        }
            while(l1!=null){
                    int y=l1.val+carry;
                    carry=0;
                         if(y>=10){

                        carry=y/10;
                        y=y%10;
                }

                 ListNode node=new ListNode(y);
                curr.next=node;
                   curr=curr.next;
                    l1=l1.next;
            }


              while(l2!=null){
                    int y=l2.val+carry;
                    carry=0;
                         if(y>=10){

                        carry=y/10;
                        y=y%10;
                }

                 ListNode node=new ListNode(y);
                curr.next=node;
                   curr=curr.next;
                    l2=l2.next;
            }
            if(carry!=0){
                     ListNode node=new ListNode(carry);
                        curr.next=node;
            }
            return dummy.next;
    

    }
}