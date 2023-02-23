class MyQueue {
    Stack<Integer> st1;
    Stack<Integer> st2;
    
    public MyQueue() {
        st1 = new Stack<Integer>();
        st2 = new Stack<Integer>();
    }
    
    public void push(int x) {
        st1.push(x);
    }
    
    public int pop() {
        while (st1.isEmpty() == false)
        {
            st2.push(st1.pop());
        }
        int i = st2.pop();
        while (st2.isEmpty() == false)
        {
            st1.push(st2.pop());
        }
        return i;
    }
    
    public int peek() {
        int i = 0;;
        while (st1.isEmpty() == false)
        {
            i = st1.peek();
            st2.push(st1.pop());
        }
        while (st2.isEmpty() == false)
        {
            st1.push(st2.pop());
        }
        return i;
    }
    
    public boolean empty() {
        return (st1.isEmpty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */