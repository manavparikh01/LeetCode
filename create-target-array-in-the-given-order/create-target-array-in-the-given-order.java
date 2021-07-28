class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] arr = new int[nums.length];
        for (int i=0;i<nums.length;i++)
        {
            if (index[i] == i)
            {
                arr[index[i]] = nums[i];
            }
            if (index[i] < i)
            {
                for (int j=nums.length-1; j>index[i];j--)
                {
                    arr[j]=arr[j-1];
                }
                arr[index[i]]=nums[i];
            }
        }
        return arr;
    }
}