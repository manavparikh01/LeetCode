class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        if (nums.length == 1)
        {
            return nums[0];
        }
        int maxpro = 1;
        int minpro = 1;
        
        for (int i=0;i<nums.length;i++)
        {
            res = Math.max(res, nums[i]);
        }
        
        for (int i=0;i<nums.length;i++)
        {
            if (nums[i] == 0)
            {
                maxpro = 1;
                minpro = 1;
            } else {
            int max = maxpro*nums[i];
            maxpro = Math.max(Math.max(maxpro*nums[i], minpro*nums[i]), nums[i]);
            minpro = Math.min(Math.min(max, minpro*nums[i]), nums[i]);
            res = Math.max(maxpro, res);
            }

        }
        
        return res;
    }
    
    // public void dp(int[] nums, int i, int sum)
    // {
    //     if (i == nums.length)
    //     {
    //         return;
    //     }
    //     sum = sum*nums[i];
    //     maxpro = Math.max(maxpro, sum);
    //     dp(nums, i + 1, sum);
    //     return;
    // }
}