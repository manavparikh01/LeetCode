class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ln = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0;i<nums.length;i++)
        {
            if (i > 0 && nums[i] == nums[i-1])
            {
                continue;
            }
            int left = i+1;
            int right = nums.length - 1;
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0)
                {
                    left += 1;
                }
                else if (sum > 0)
                {
                    right -= 1;
                }
                else
                {
                    List<Integer> li = new ArrayList<>();
                    li.add(nums[i]);
                    li.add(nums[left]);
                    li.add(nums[right]);
                    ln.add(li);
                    left += 1;
                    while (nums[left] == nums[left-1] && left < right)
                    {
                        left += 1;
                    }
                }
            }
        }
        return ln;
    }
}