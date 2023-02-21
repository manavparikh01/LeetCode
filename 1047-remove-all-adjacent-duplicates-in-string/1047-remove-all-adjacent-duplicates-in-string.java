class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> st = new Stack<Character>();
        st.push(s.charAt(s.length() -1));
        for (int i = s.length()-2;i>=0;i--)
        {
            if (st.isEmpty() == false)
            {
                if (s.charAt(i) == st.peek())
            {
                st.pop();
            }
            else
            {
                st.push(s.charAt(i));
            }
            }
            else
            {
                st.push(s.charAt(i));
            }
            
        }
        String ss = "";
        while (st.isEmpty() == false)
        {
            ss = ss + st.pop();
        }
        return ss;
    }
}