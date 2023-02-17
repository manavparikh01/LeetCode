class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        for (int i =0 ;i<s.length();i++)
        {
            char m = s.charAt(i);
            if (m == '(' || m == '{' || m == '[')
            {
                st.push(m);
            }
            else
            {
                if (st.isEmpty() == true)
                {
                    return false;
                }
                else if (isMatching(st.peek(), m) == false)
                {
                    return false;
                }
                else
                {
                    st.pop();
                }
            }   
        }
        if (st.isEmpty() == true)
        {
            return true;
        }
        return false;
    }
    public boolean isMatching(Character a, Character b)
    {
        return ((a == '(' && b == ')') || (a == '{' && b == '}') || (a == '[' && b == ']'));
    }
}