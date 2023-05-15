class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> al = new ArrayList<Integer>();
        if (nums.length == 0)
        {
            return al;
        }
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int i = 0;i<nums.length;i++)
        {
            hs.add(nums[i]);
        }
        for (int i = 1;i<=nums.length;i++)
        {
            if (!hs.contains(i))
            {
                al.add(i);
            }
        }
        return al;
    }
}