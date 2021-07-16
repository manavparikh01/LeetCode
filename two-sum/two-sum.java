class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = nums.length;
        int sum = 0;
        String str = null;
        // int[] result;
        int a = 0,b = 0;
        for (int i = 0; i < l; i++) 
        {
            for (int j = i + 1; j < l; j++)
            {
                sum = nums[i] + nums[j];
                if (sum == target)
                {
                    // result[0] = i;
                    // result[1] = j;
                    // //str = '['+String.valueOf(i)+','+String.valueOf(j)+']';
                    a = i;
                    b = j;
                }
                
            }
        }
        int[] arr = new int[2];
        arr[0] = a;
        arr[1] = b;
        return arr;
    
    }
}