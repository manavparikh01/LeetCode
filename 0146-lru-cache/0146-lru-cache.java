class Node {
    int key;
    int val;
    Node next;
    Node prev;
    Node (int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    HashMap<Integer, Node> hm;
    int size;
    Node left;
    Node right;

    public LRUCache(int capacity) {
        hm = new HashMap<Integer, Node>();
        size = capacity;
        left = new Node(0,0);
        right = new Node(0,0);
        left.next = right;
        right.prev = left;
    }
    
    public void remove(Node curr) {
        Node prev = curr.prev;
        Node next = curr.next;
        prev.next = next;
        next.prev = prev;
    }
    
    public void insert(Node curr) {
        Node prev = right.prev;
        prev.next = curr;
        curr.prev = prev;
        curr.next = right;
        right.prev = curr;
    }
    
    public int get(int key) {
        if (hm.containsKey(key))
        {
            //System.out.println(key);
            remove(hm.get(key));
            insert(hm.get(key));
            return hm.get(key).val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (hm.containsKey(key))
        {
            remove(hm.get(key));
        }
        Node newNod = new Node(key, value);
        hm.put(key, newNod);
        insert(newNod);
        //System.out.println(key + " " + hm.size());
        if (hm.size() > size)
        {
            Node lru = left.next;
            remove(lru);
            hm.remove(lru.key);
        }
        //System.out.println(key + " " + hm.size() + " g");
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */