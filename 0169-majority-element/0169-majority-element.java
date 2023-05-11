class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1)
        {
            return nums[0];
        }
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for (int i = 0;i<nums.length;i++)
        {
            if (!hm.containsKey(nums[i]))
            {
                hm.put(nums[i], 1);
            }
            else
            {
                int n = hm.get(nums[i]);
                n++;
                hm.put(nums[i], n);
            }
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> m : hm.entrySet())
        {
            //System.out.println(m.getKey() + " " + m.getValue());
            if (m.getValue() > nums.length / 2)
            {
                max = m.getKey();
            }
        }
        return max;
    }
}