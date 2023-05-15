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
            hs.add(i+1);
        }
        for (int i = 0;i<nums.length;i++)
        {
            if (hs.contains(nums[i]))
            {
                hs.remove(nums[i]);
            }
        }
        for (Integer s : hs)
        {
            al.add(s);
        }
        return al;
    }
}