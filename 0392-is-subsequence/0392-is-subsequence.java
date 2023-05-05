class Solution {
    public boolean isSubsequence(String s, String t) {
        Stack<Character> st = new Stack<Character>();
        for (int i = 0;i<s.length();i++)
        {
            st.push(s.charAt(i));
        }
        for (int i = t.length() -1;i>=0;i--)
        {
            if (st.isEmpty())
            {
                break;
            }
            if (t.charAt(i) == st.peek())
            {
                st.pop();
            }
        }
        return st.isEmpty();
    }
}