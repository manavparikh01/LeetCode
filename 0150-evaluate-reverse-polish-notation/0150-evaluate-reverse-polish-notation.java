class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<Integer>();
        for (int i = 0;i<tokens.length;i++)
        {
            if (!tokens[i].equals("+") && !tokens[i].equals("-") && !tokens[i].equals("*") && !tokens[i].equals("/"))
            {
                st.push(Integer.parseInt(tokens[i]));
            }
            if (tokens[i].equals("+"))
            {
                int b = st.peek();
                st.pop();
                int a  = st.peek();
                st.pop();
                int c = a + b;
                st.push(c);
            }
            if (tokens[i].equals("-"))
            {
                int b = st.peek();
                st.pop();
                int a  = st.peek();
                st.pop();
                int c = a - b;
                st.push(c);
            }
            if (tokens[i].equals("*"))
            {
                int b = st.peek();
                st.pop();
                int a  = st.peek();
                st.pop();
                int c = a * b;
                st.push(c);
            }
            if (tokens[i].equals("/"))
            {
                int b = st.peek();
                st.pop();
                int a  = st.peek();
                st.pop();
                int c = a / b;
                st.push(c);
            }
        }
        return st.peek();
    }
}