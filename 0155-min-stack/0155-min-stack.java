class MinStack {
    ArrayList<Integer> al;
    int size = 0;

    public MinStack() {
        al = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        al.add(val);
        size++;
    }
    
    public void pop() {
        al.remove(size-1);
        size--;
    }
    
    public int top() {
        return al.get(size-1);
        
    }
    
    public int getMin() {
        // int min = al.get(0);
        // for (int i = 1;i<size;i++)
        // {
        //     if (al.get(i) < min)
        //     {
        //         min = al.get(i);
        //     }
        // }
        // return min;
        return Collections.min(al);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */