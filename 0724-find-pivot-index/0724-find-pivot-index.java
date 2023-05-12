class Solution {
    public int pivotIndex(int[] nums) {
        if (nums.length == 0)
        {
            return -1;
        }
        int right = 0;
        int left = 0;
        for (int i = 0;i<nums.length;i++)
        {
            right += nums[i];
        }
        for (int i = 0;i<nums.length;i++)
        {
            
            right = right - nums[i];
            if (i >0)
            {
                left = left + nums[i-1];
            }
            //System.out.println(left + " " + right);
            if (left == right)
            {
                return i;
            }
        }
        
        return -1;
    }
}