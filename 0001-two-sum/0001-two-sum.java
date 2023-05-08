class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        int arr[] = new int[2];
        for (int i = 0;i<nums.length;i++)
        {
            if (hm.containsKey(target - nums[i]))
            {
                arr[0] = hm.get(target - nums[i]);
                arr[1] = i;
            }
            else
            {
                hm.put(nums[i], i);
            }
        }
        return arr;
    }
}