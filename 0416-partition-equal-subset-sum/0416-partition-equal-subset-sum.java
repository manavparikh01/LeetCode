class Solution {

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int i = 0; i< nums.length;i++)
        {
            sum += nums[i];
        }
        if (sum % 2 == 1)
        {
            return false;
        }
        HashSet<Integer> hs = new HashSet<Integer>();
        hs.add(0);
        hs.add(nums[nums.length-1]);
        for (int i = nums.length-2;i>=0;i--)
        {
            HashSet<Integer> hss = new HashSet<Integer>();
            for (int element: hs)
            {
                int sum1 = nums[i] + element;
                if (sum1 == sum/2)
                {
                    return true;
                }
                else
                {
                    hss.add(sum1);
                }
            }
            for (int element: hss)
            {
                hs.add(element);
            }
        }
        return false;
    }
}