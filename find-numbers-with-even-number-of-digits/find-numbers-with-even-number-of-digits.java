class Solution {
    public int findNumbers(int[] nums) {
        int num;
        int sum=0;
        int length;
        for (int i=0;i<nums.length;i++)
        {
            num=nums[i];
            num=Math.abs(num);
            length=String.valueOf(num).length();
            if (length%2 == 0)
            {
                sum++;
            }
        }
        return sum;
    }
}