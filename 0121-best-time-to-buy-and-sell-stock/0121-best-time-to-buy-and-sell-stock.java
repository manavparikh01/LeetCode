class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0)
        {
            return 0;
        }
        int arr[] = new int[prices.length];
        int max = 0;
        int maxsell = prices[prices.length - 1];
        arr[prices.length - 1] = maxsell;
        for (int i = prices.length - 2;i>=0;i--)
        {
            if (prices[i] > maxsell)
            {
                maxsell = prices[i];
            }
            arr[i] = maxsell;
        }
        
        for (int i = 0;i<prices.length;i++)
        {
            int diff = arr[i] - prices[i];
            max = Math.max(max, diff);
        }
        if (max <= 0)
        {
            return 0;
        }
        return max;
    }
}