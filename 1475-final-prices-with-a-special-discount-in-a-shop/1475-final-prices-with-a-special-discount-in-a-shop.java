class Solution {
    public int[] finalPrices(int[] prices) {
        Stack<Integer> st = new Stack<Integer>();
        int[] arr = new int[prices.length];
        st.push(prices[prices.length-1]);
        arr[prices.length-1] = -1;
        for (int i = prices.length -2;i>=0;i--)
        {
            while (st.isEmpty() == false && prices[i]<st.peek())
            {
                st.pop();
            }
            int next = (st.isEmpty() == true)?(-1):(st.peek());
            arr[i] = next;
            st.push(prices[i]);
        }
        for (int  i = 0;i<prices.length;i++)
        {
            if (arr[i] != -1)
            {
                prices[i] = prices[i] - arr[i];
            }
        }
        return prices;
    }
}