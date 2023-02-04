class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int count[] = new int[nums.length];
        for (int i =0;i<nums.length;i++)
        {
            count[i] = nums[i];
        }
        int res[] = new int[nums.length];
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        Arrays.sort(count);
        int j=0;
        for (int i=0;i<nums.length;i++)
        {
            hm.put(count[i], j);
            while (i+1 < nums.length && count[i] == count[i+1])
            {
                i++;
            }
            j = i+1;
            System.out.print(i);
            System.out.print(" ");
            System.out.println(j);
        }
        //hm.put(count[nums.length-1], j);
        for (int i=0;i<nums.length;i++)
        {
            System.out.println(hm.get(nums[i]));
            res[i] = hm.get(nums[i]);
        }
        return res;
    }
}