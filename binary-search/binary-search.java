class Solution {
    public int search(int[] nums, int target) {
        int i =0;
        int max = -1;
        int num = nums.length-1;
        while(i<=num) {
            int m = i + (num - i)/2;
            if (nums[m] == target)
            {
                max = m;
                return max;
            }
            if (nums[m] > target)
            {
                num = m -1;
            }
        else {
            i = m + 1;
        }
        }
             
        return max;
        
    }
}