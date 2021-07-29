class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] arr = new int[nums.length];
        for (int i=0;i<nums.length-1;i++)
        {
            
            for (int j = 0; j < nums.length-i-1; j++)
                if (nums[j]%2==1 && nums[j+1]%2==0)
                {
                    // swap arr[j+1] and arr[j]
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
    
        }
        return nums;
    }
}