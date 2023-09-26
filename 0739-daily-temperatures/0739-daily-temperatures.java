class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> st = new Stack<Integer>();
        int arr[] = new int[temperatures.length];
        for (int i = temperatures.length - 1;i>=0;i--)
        {
            while (st.isEmpty() == false && temperatures[st.peek()] <= temperatures[i])
            {
                st.pop();
            }
            if (st.isEmpty() == true)
            {
                arr[i] = 0;
            }
            else
            {
                arr[i] = st.peek() - i;
            }
            st.push(i);
        }
        return arr;
    }
}