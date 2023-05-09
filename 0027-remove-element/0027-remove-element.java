class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        ArrayList<Integer> hs = new ArrayList<Integer>();
        for (int i = 0;i<nums.length;i++)
        {
            if (nums[i] != val)
            {
                hs.add(nums[i]);
                k++;
            }
        }
        int j = 0;
        for (j = 0;j<hs.size();j++)
        {
            nums[j] = hs.get(j);
        }
        while (j < nums.length -1)
        {
            j++;
            nums[j] = val -1;
        }
        return k;
    }
}