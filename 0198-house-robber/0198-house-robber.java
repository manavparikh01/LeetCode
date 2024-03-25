class Solution {
    public int rob(int[] nums) {
        int[] arr = new int[nums.length+1];
        for (int i = 0;i<nums.length;i++)
        {
            arr[i] = nums[i];
        }
        arr[nums.length] = 0;
        for (int i = arr.length-3;i>-1;i--)
        {
            arr[i] = Math.max(arr[i]+arr[i+2], arr[i+1]);
        }
        return arr[0];
    }
}