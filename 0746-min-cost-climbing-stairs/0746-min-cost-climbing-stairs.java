class Solution {
    
    public int minCostClimbingStairs(int[] cost) {
        int[] arr = new int[cost.length+1];
        for (int i = 0;i<cost.length;i++)
        {
            arr[i] = cost[i];
        }
        arr[cost.length] = 0;
        for (int i = arr.length - 3;i>-1;i--)
        {
            arr[i] += Math.min(arr[i+1], arr[i+2]);
        }
        
        return Math.min(arr[0], arr[1]);
    }
}