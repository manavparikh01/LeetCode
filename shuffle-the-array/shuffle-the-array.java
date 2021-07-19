;class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] arr=new int[2*n];
        int count=0;
        for (int i=0;i<2*n;i++)
        {
            if (i<n)
            {
                arr[i*2]=nums[i];
            } else {
                count++;
                {
                    arr[((i-n)+count)]=nums[i];
                }
                
                
            }
        };
        for (int i=0;i<2*n;i++)
        {
            nums[i]=arr[i];
        };
        return nums;
    }
}


//////////////
// 0 1 2 3 4 5 6 7
// 1 2 3 4 4 3 2 1
// 1 4 2 4 3 2 4 1