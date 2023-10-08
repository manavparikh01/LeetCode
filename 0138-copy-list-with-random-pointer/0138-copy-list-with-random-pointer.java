/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null)
        {
            return null;
        }
        HashMap<Node, Node> hm = new HashMap<Node, Node>();
        Node curr = head;
        Node curr1 = new Node(curr.val);
        Node curr2 = curr1;
        hm.put(curr, curr1);
        while (curr != null)
        {
            if (curr.next == null)
            {
                curr1.next = null;
                break;
            }
            Node newNex = new Node(curr.next.val);
            curr1.next = newNex;
            curr = curr.next;
            curr1 = curr1.next;
            hm.put(curr, curr1);
        }
        Node curr3 = head;
        Node curr4 = curr2;
        while (curr3 != null)
        {
            if (curr3.random == null)
            {
                curr4.random = null;
            }
            else
            {
                //System.out.println(curr3.random.val);
                curr4.random = hm.get(curr3.random);
            }
            curr3 = curr3.next;
            curr4 = curr4.next;
        }
        return curr2;
    }
}