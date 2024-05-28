class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] arr = new boolean[nums.length];
        for (int i = 0;i<nums.length;i++)
        {
            if (arr[nums[i]-1] == true)
            {
                return nums[i];
            }
            else
            {
                arr[nums[i]-1] = true;
            }
        }
        return -1;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // int slow = 0;
        // int fast = 0;
        // do
        // {
        //     slow = nums[slow];
        //     fast = nums[nums[fast]];
        // } while (slow != fast);
        // int slow1 = 0;
        // do
        // {
        //     slow = nums[slow];
        //     slow1 = nums[slow1];
        // } while (slow != slow1);
        // return slow;
    }
}