class Solution {
    public int specialArray(int[] nums) {
        // int[] arr = new int[nums.length];
        // arr = nums;
        // Arrays.sort(arr);
        // int sum = 0;
        // int x = 0;
        // for (int i=0;i<arr.length;i++) {
        //     while (i<arr.length-1 && arr[i]==arr[i+1])
        //     {
        //         i++;
        //     }
        //     sum++;
        // }
        // Arrays.sort(nums);
        // int max = nums[nums.length-1];
        int j = 0;
        //int x = 0;
        int max = 0;
        while (j<=nums.length){
            int x=0;
            for (int i=0;i<nums.length;i++)
        {
            if (nums[i]>=j)
            {
                x++;
            }
                
        }
            //System.out.println(x + "hehe" + j);
            if (x==j)
                {
                
                    max=x;
                return max;
                }
            else {
                max =0;
            }
            //System.out.println(max);
            j++;
        }
        
        if (max>0)
        {
            return max;
        }
        else {
            return -1;
        }
    }
}