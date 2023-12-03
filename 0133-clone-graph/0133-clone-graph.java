/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null)
        {
            return null;
        }
        if (node.neighbors.size() == 0)
        {
            return new Node(node.val);
        }
        Node curr = new Node(node.val);
        Node head = curr;
        HashMap<Integer, Node> h = new HashMap<Integer, Node>();
        ArrayList<Integer> al = new ArrayList<Integer>();
        h.put(node.val, curr);
        al.add(node.val);
        Queue<Node> q = new LinkedList<Node>();
        q.add(node);
        while (q.isEmpty() == false)
        {
            Node now = q.element();
            q.remove();
            int length = now.neighbors.size();
            ArrayList<Node> all = new ArrayList<Node>();
            for (int i = 0;i<length;i++)
            {
                Node again = now.neighbors.get(i);
                if (h.containsKey(again.val))
                {
                    all.add(h.get(again.val));
                }
                else
                {
                    q.add(again);
                    Node currently = new Node(again.val);
                    all.add(currently);
                    h.put(again.val, currently);
                }
            }
            if (h.containsKey(now.val))
            {
                int l = all.size();
                for (int a = 0;a<l;a++)
                {
                    h.get(now.val).neighbors.add(all.get(a));
                }
            }
            else
            {
                Node cur = new Node(now.val, all);
                h.put(now.val, cur);
            }
        }
        return head;
    }
}