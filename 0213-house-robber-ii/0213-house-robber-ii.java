class Solution {
    public int rob(int[] nums) {
        if (nums.length < 2)
        {
            return nums[0];
        }
        int m = robb(nums);
        int n = robb1(nums);
        return Math.max(m, n);
    }
    
    public int robb(int[] nums)
    {
        int[] arr = new int[nums.length];
        for (int i = 0;i<nums.length-1;i++)
        {
            arr[i] = nums[i];
        }
        arr[nums.length-1] = 0;
        for (int i = arr.length-3;i>-1;i--)
        {
            arr[i] = Math.max(arr[i]+arr[i+2], arr[i+1]);
        }
        return arr[0];
    }
    
    public int robb1(int[] nums)
    {
        int[] arr = new int[nums.length];
        for (int i = 1;i<nums.length;i++)
        {
            arr[i-1] = nums[i];
        }
        arr[nums.length-1] = 0;
        for (int i = arr.length-3;i>-1;i--)
        {
            arr[i] = Math.max(arr[i]+arr[i+2], arr[i+1]);
        }
        return arr[0];
    }
}