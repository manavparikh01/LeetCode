class Solution {
    class Pair {
        int index;
        int value;
        Pair (int a, int b)
        {
            index = a;
            value = b;
        }
    }
    public int largestRectangleArea(int[] heights) {
        Stack<Pair> st = new Stack<Pair>();
        st.push(new Pair(0, heights[0]));
        int h = 0;
        for (int i = 1;i<heights.length;i++)
        {
            int curr = i;
            while (st.isEmpty() == false && st.peek().value > heights[i])
            {
                Pair p = st.peek();
                int a  = p.value * (i - p.index);
                curr = p.index;
                h = Math.max(h, a);
                //System.out.println(h + " " + p.value + " " + p.index + " " + i);
                st.pop();
            }
            st.push(new Pair(curr, heights[i]));
            Pair pp = st.peek();
            //System.out.println(pp.index + " " + pp.value);
        }
        while (st.isEmpty() == false)
        {
            Pair p = st.peek();
            int a = p.value * (heights.length - p.index);
            h = Math.max(h, a);
            //System.out.println(h + " " + p.value + " " + p.index + " " + heights.length);
            st.pop();
        }
        return h;
    }
}