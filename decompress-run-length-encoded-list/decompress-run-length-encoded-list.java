class Solution {
    public int[] decompressRLElist(int[] nums) {
        int num;
        ArrayList<Integer> str = new ArrayList<Integer>();
        for (int i=0;i<nums.length-1;i+=2)
        {
            num=nums[i];
            for (int j=0;j<num;j++)
            {
                str.add(nums[i+1]);
            }
        }
        // int[] arr = new int[str.size()];
        // arr = str.toArray(arr);
        int[] arr = str.stream().mapToInt(i->i).toArray();
        return arr;
    }
}